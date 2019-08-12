from application import app, db
from application.logs.models import Log
from application.logs.forms import LogForm

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

def total_workhours(logs):
    total = 0
    for log in logs:
        total += log.duration
    return total

@app.route("/<course_id>/logs/", methods=["GET"])
@login_required
def logs_index(course_id):
    l = Log.query.filter_by(user_id=current_user.id, course_id=course_id)
    d = total_workhours(l)
    return render_template("logs/list.html", course_id=course_id, logs = l, duration = d)

@app.route("/<course_id>/logs/new/")
@login_required
def logs_form(course_id):
    return render_template("logs/new.html", course_id=course_id, form = LogForm())

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y'):
    return value.strftime(format)

@app.route("/<course_id>/logs/<log_id>/", methods=["GET"])
@login_required
def logs_log(course_id, log_id):
    l = Log.query.get(log_id)

    return render_template("logs/log.html", log = l)

@app.route("/logs/courses/", methods=["GET"])
@login_required
def logs_courses():
    return render_template("logs/courses.html")

@app.route("/<course_id>/logs/", methods=["POST"])
@login_required
def logs_create(course_id):
    form = LogForm(request.form)

    if not form.validate():
        return render_template("/logs/new.html", form = form)

    l = Log(form.description.data, form.duration.data)
    l.user_id = current_user.id
    l.course_id = course_id

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/update", methods=["POST"])
@login_required
def logs_update(course_id, log_id):
    description = request.form.get("description")
    duration = request.form.get("duration")

    l = Log.query.get(log_id)
    if description:
        l.description = description

    if duration != "":
        l.duration = duration

    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/increment", methods=["POST"])
@login_required
def logs_increment(course_id, log_id):
    duration = request.form.get("duration")
    l = Log.query.get(log_id)

    if duration != "":
        l.duration += float(duration)

    db.session().commit()

    return redirect(url_for("logs_index", course_id = course_id))

@app.route("/<course_id>/logs/<log_id>/delete/", methods=["POST"])
@login_required
def logs_delete(course_id, log_id):
    print('id: ' + log_id)
    Log.query.filter_by(id=log_id).delete()
    db.session.commit()

    return redirect(url_for("logs_index", course_id = course_id))
