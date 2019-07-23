from application import app, db
from flask import render_template, request, redirect, url_for
from application.logs.models import Log

@app.route("/logs", methods=["GET"])
def logs_index():
    return render_template("logs/list.html", logs =  Log.query.all())

@app.route("/logs/new/")
def logs_form():
    return render_template("logs/new.html")

@app.route("/logs/<log_id>/", methods=["POST"])
def logs_update(log_id):
    duration = request.form.get("duration")

    l = Log.query.get(log_id)
    l.duration = duration
    db.session().commit()

    return redirect(url_for("logs_index"))

@app.route("/logs/", methods=["POST"])
def logs_create():
    l = Log(request.form.get("name"), request.form.get("duration"))

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("logs_index"))
