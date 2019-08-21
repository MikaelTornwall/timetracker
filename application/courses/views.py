from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.courses.models import Course
from application.auth.models import User
from application.courses.forms import CourseForm

# Views for student
@app.route("/courses/", methods=["GET"])
@login_required(role="STUDENT")
def courses_index():
    courses = Course.count_enrolled_students_in_each_course()
    mycourses = User.query.get(current_user.id).courses

    course_array = []

    for course in mycourses:
        course_array.append(course.course_id)

    length = Course.count_courses()

    return render_template("courses/courses.html", courses = courses, mycourses = course_array, length = length)

@app.route("/courses/<course_id>/enroll/", methods=["GET"])
@login_required(role="STUDENT")
def course_enroll(course_id):
    c = Course.query.get(course_id)
    u = User.query.get(current_user.id)

    if u in c.users:
        c.users.remove(u)
    else:
        c.users.append(u)

    db.session.commit()

    return redirect(url_for("courses_index"))

# Views for teacher and student
@app.route("/courses/<course_id>/", methods=["GET"])
@login_required()
def courses_course(course_id):
    c = Course.query.get(course_id)

    if current_user.is_teacher():
        s = c.find_students(course_id)
        l = c.count_students(course_id)

        return render_template("courses/course.html", course = c, students = s, length = l)

    a = Course.query.all()
    m = User.query.get(current_user.id).courses

    return render_template("courses/course.html", course = c, courses = a, mycourses = m)

# Views for teacher
@app.route("/courses/mycourses", methods=["GET"])
@login_required(role="TEACHER")
def courses_mycourses():
    c = User.query.get(current_user.id)
    length = c.count_users_courses(current_user)
    return render_template("courses/mylist.html", courses = c.courses, length = length)

@app.route("/courses/new/")
@login_required(role="TEACHER")
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/", methods=["POST"])
@login_required(role="TEACHER")
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("/courses/new.html", form = form)

    c = Course(form.course_id.data, form.title.data, form.description.data, form.duration.data, form.deadline.data)
    u = User.query.get(current_user.id)

    c.users.append(u)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_mycourses"))

@app.route("/courses/<course_id>/edit", methods=["GET"])
@login_required(role="TEACHER")
def courses_edit(course_id):
    c = Course.query.get(course_id)

    return render_template("courses/edit.html", course = c, form = CourseForm())

@app.route("/courses/<course_id>/update", methods=["POST"])
@login_required(role="TEACHER")
def courses_update(course_id):
    form = CourseForm(request.form)
    c = Course.query.get(course_id)

    if not form.validate():
        return render_template("/courses/edit.html", course=c, form = form)

    c.course_id = form.course_id.data
    c.title = form.title.data
    c.description = form.description.data
    c.duration = form.duration.data
    c.deadline = form.deadline.data

    db.session().commit()

    return redirect(url_for("courses_course", course_id = course_id))

@app.route("/courses/<course_id>/delete/", methods=["POST"])
@login_required(role="TEACHER")
def courses_delete(course_id):
    c = Course.query.filter_by(id=course_id).first()

    if (c is not None):
        db.session.delete(c)
        db.session.commit()

    return redirect(url_for("courses_mycourses"))
