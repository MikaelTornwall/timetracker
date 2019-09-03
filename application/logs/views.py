from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.logs.models import Log
from application.logs.forms import LogForm
from application.courses.models import Course
from application.auth.models import User

# Views for student
@app.route("/logs/", methods=["GET"])
@login_required(role="STUDENT")
def logs_all():
    active_courses = Log.fetch_students_courses_with_progress()
    inactive_courses = Course.fetch_users_courses_without_logs()
    return render_template("logs/logs.html", active_courses = active_courses, inactive_courses = inactive_courses)

@app.route("/<course_id>/logs/", methods=["GET"])
@login_required(role="STUDENT")
def logs_index(course_id):
    logs = Log.find_logs_of_course(course_id, current_user.id)
    duration = Log.total_workhours(course_id, current_user.id)

    if not duration:
        duration = 0

    course = Course.query.get(course_id)

    return render_template("logs/list.html", course = course, course_id = course_id, logs = logs, duration = round(duration, 1), desc=False)

@app.route("/<course_id>/logs/desc", methods=["GET"])
@login_required(role="STUDENT")
def logs_index_desc(course_id):
    logs = Log.find_logs_of_course_desc(course_id, current_user.id)
    duration = Log.total_workhours(course_id, current_user.id)

    if not duration:
        duration = 0

    course = Course.query.get(course_id)

    return render_template("logs/list.html", course = course, course_id = course_id, logs = logs, duration = round(duration, 1), desc=True)


@app.route("/<course_id>/logs/new/")
@login_required(role="STUDENT")
def logs_form(course_id):
    return render_template("logs/new.html", course_id = course_id, form = LogForm())

@app.route("/<course_id>/logs/<log_id>/", methods=["GET"])
@login_required(role="STUDENT")
def logs_log(course_id, log_id):
    log = Log.query.get(log_id)

    return render_template("logs/log.html", log = log)

@app.route("/<course_id>/logs/", methods=["POST"])
@login_required(role="STUDENT")
def logs_create(course_id):
    form = LogForm(request.form)

    if not form.validate():
        return render_template("/logs/new.html", form = form, course_id = course_id)

    log = Log(form.description.data, form.duration.data)
    log.user_id = current_user.id
    log.course_id = course_id

    db.session().add(log)
    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/update", methods=["POST"])
@login_required(role="STUDENT")
def logs_update(course_id, log_id):
    description = request.form.get("description")
    duration = request.form.get("duration")

    log = Log.query.get(log_id)
    if description:
        log.description = description

    if duration != "":
        log.duration = duration

    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/increment", methods=["POST"])
@login_required(role="STUDENT")
def logs_increment(course_id, log_id):
    duration = request.form.get("duration")
    log = Log.query.get(log_id)

    if duration != "":
        log.duration += float(duration)

    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/delete/", methods=["POST"])
@login_required(role="STUDENT")
def logs_delete(course_id, log_id):
    log = Log.query.filter_by(id=log_id).first()

    if (log is not None):
        db.session.delete(log)
        db.session.commit()

    return redirect(url_for("logs_index", course_id = course_id))

# Views for teacher
@app.route("/<course_id>/logs/<user_id>/log/", methods=["GET"])
@login_required(role="TEACHER")
def logs_course_user(course_id, user_id):
    logs = Log.find_logs_of_course(course_id, user_id)
    duration = Log.total_workhours(course_id, user_id)
    course = Course.query.get(course_id)
    user = User.query.get(user_id)

    return render_template("logs/list.html", course = course, course_id = course_id, logs = logs, duration = duration, student = user)

# Filters
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y'):
    return value.strftime(format)

@app.template_filter('datetimeformat_with_time')
def datetimeformat_with_time(value, format='%B %d, %Y at %H:%M'):
    return value.strftime(format)

@app.template_filter('updatedateformat')
def updatedateformat(value, format='%d.%m.%Y %H:%M'):
    return value.strftime(format)
