from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Student
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login/student", methods=["GET", "POST"])
def auth_studentLogin():
    if request.method == "GET":
        return render_template("auth/studentLogin.html", form = LoginForm())

    form = LoginForm(request.form)

    student = Student.query.filter_by(email=form.email.data, password=form.password.data).first()

    if not student:
        return render_template("auth/studentLogin.html", form = form, error = "Incorrect email address or password")

    login_user(student)
    return redirect(url_for("index"))

@app.route("/auth/logout/student")
def auth_studentLogout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup/student", methods=["GET", "POST"])
def auth_studentSignup():
    if request.method == "GET":
        return render_template("auth/studentSignup.html", form = SignupForm())

    form = SignupForm(request.form)

    print(form)

    if not form.validate():
        return render_template("auth/studentSignup.html", form = form, error = "Remember to fill all the fields")

    s = Student(form.studentId.data, form.firstname.data, form.lastname.data, form.email.data, form.password.data)

    db.session.add(s)
    db.session.commit()

    return redirect(url_for("auth_studentLogin"))
