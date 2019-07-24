from application import app, db
from flask import render_template, request, redirect, url_for
from application.logs.models import Log

@app.route("/logs", methods=["GET"])
def logs_index():
    return render_template("logs/list.html", logs =  Log.query.all())

@app.route("/logs/new/")
def logs_form():
    return render_template("logs/new.html")

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y'):
    return value.strftime(format)

@app.route("/logs/<log_id>/", methods=["POST"])
def logs_update(log_id):
    description = request.form.get("description")
    duration = request.form.get("duration")

    l = Log.query.get(log_id)
    if description:
        l.description += " "
        l.description += description

    if duration != "":
        l.duration = duration

    db.session().commit()

    return redirect(url_for("logs_index"))

@app.route("/logs/", methods=["POST"])
def logs_create():
    l = Log(request.form.get("description"), request.form.get("duration"))

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("logs_index"))
