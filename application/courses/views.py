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

@app.route("/courses/search", methods=["POST"])
@login_required(role="STUDENT")
def courses_search():
    search_term = request.form.get("search")
    courses = Course.count_enrolled_students_in_each_course_with_search_term(search_term)
    mycourses = User.query.get(current_user.id).courses

    mycourses_array = []

    for course in mycourses:
        mycourses_array.append(course.course_id)

    course_array = []

    length = len(courses)

    return render_template("courses/courses.html", courses = courses, mycourses = mycourses_array, length = length)


@app.route("/courses/<course_id>/enroll/", methods=["GET"])
@login_required(role="STUDENT")
def course_enroll(course_id):
    course = Course.query.get(course_id)
    user = User.query.get(current_user.id)

    if user in course.users:
        course.users.remove(user)
    else:
        course.users.append(user)

    db.session.commit()

    return redirect(url_for("courses_index"))

# Views for teacher and student
@app.route("/courses/<course_id>/", methods=["GET"])
@login_required()
def courses_course(course_id):
    course = Course.query.get(course_id)

    if current_user.is_teacher():
        students = course.find_students(course_id)
        length = course.count_students(course_id)

        return render_template("courses/course.html", course = course, students = students, length = length)

    courses = Course.query.all()
    mycourses = User.query.get(current_user.id).courses

    return render_template("courses/course.html", course = course, courses = courses, mycourses = mycourses)

# Views for teacher
@app.route("/courses/mycourses", methods=["GET"])
@login_required(role="TEACHER")
def courses_mycourses():
    user = User.query.get(current_user.id)
    length = user.count_users_courses(current_user)
    return render_template("courses/mylist.html", courses = user.courses, length = length)

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
    course = Course.query.get(course_id)

    return render_template("courses/edit.html", course = course, form = CourseForm())

@app.route("/courses/<course_id>/update", methods=["POST"])
@login_required(role="TEACHER")
def courses_update(course_id):
    form = CourseForm(request.form)
    course = Course.query.get(course_id)

    if not form.validate():
        return render_template("/courses/edit.html", course = course, form = form)

    course.course_id = form.course_id.data
    course.title = form.title.data
    course.description = form.description.data
    course.duration = form.duration.data
    course.deadline = form.deadline.data

    db.session().commit()

    return redirect(url_for("courses_course", course_id = course_id))

@app.route("/courses/<course_id>/delete/", methods=["POST"])
@login_required(role="TEACHER")
def courses_delete(course_id):
    course = Course.query.filter_by(id=course_id).first()

    if (course is not None):
        db.session.delete(course)
        db.session.commit()

    return redirect(url_for("courses_mycourses"))
