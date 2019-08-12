from application import app, db
from application.courses.models import Course
from application.auth.models import User
from application.courses.forms import CourseForm

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

@app.route("/courses/", methods=["GET"])
@login_required
def courses_index():
    c = Course.query.all()
    return render_template("courses/list.html", courses = c)

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<course_id>/", methods=["GET"])
@login_required
def courses_course(course_id):
    c = Course.query.get(course_id)

    return render_template("courses/course.html", course = c)

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required
def course_enroll(course_id):
    # Opiskelijan kurssi-ilmoittautuminen
    c = Course.query.get(course_id)

    return render_template("courses/course.html", course = c)

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("/courses/new.html", form = form)

    c = Course(form.courseId.data, form.title.data, form.description.data, form.duration.data, form.deadline.data)
    u = User.query.get(current_user.id)

    # u.courses.append(c)
    c.users.append(u)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/edit", methods=["GET"])
@login_required
def courses_edit(course_id):
    c = Course.query.get(course_id)

    return render_template("courses/edit.html", course = c, form = CourseForm())

@app.route("/courses/<course_id>/update", methods=["POST"])
@login_required
def courses_update(course_id):
    form = CourseForm(request.form)
    c = Course.query.get(course_id)

    if not form.validate():
        return render_template("/courses/edit.html", course=c, form = form)

    c.courseId = form.courseId.data
    c.title = form.title.data
    c.description = form.description.data
    c.duration = form.duration.data
    c.deadline = form.deadline.data

    db.session().commit()

    return redirect(url_for("courses_index", course_id = course_id))

@app.route("/courses/<course_id>/delete/", methods=["POST"])
@login_required
def courses_delete(course_id):
    print('id: ' + course_id)
    c = Course.query.filter_by(id=course_id).first()
    #c.users.clear()
    if (c is not None):
        db.session.delete(c)
        db.session.commit()

    return redirect(url_for("courses_index"))
