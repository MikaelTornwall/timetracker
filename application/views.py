from flask import render_template
from application import app
from flask_login import current_user
from application.auth.models import User
from application.courses.models import Course
from application.logs.models import Log

@app.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("index.html")

    user = User.query.get(current_user.id)
    name = user.firstname + ' ' + user.lastname

    if user.is_student():
        courses = Log.fetch_five_most_recent_courses_with_activity()
        return render_template("index.html", name = name, courses = courses)

    if user.is_teacher():
        courses = Course.fetch_five_most_recent_courses()
        return render_template("index.html", name = name, courses = courses)

    return render_template("index.html")
