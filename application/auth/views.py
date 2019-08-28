from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User, Role
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/login.html", form = form, error = "Remember to fill all the fields")

    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()

    if not user:
        return render_template("auth/login.html", form = form, error = "Incorrect email address or password")

    login_user(user)

    app.jinja_env.globals.update(is_student=current_user.is_student())
    app.jinja_env.globals.update(is_teacher=current_user.is_teacher())

    return redirect(url_for("index"))

@app.route("/auth/signup/", methods=["GET", "POST"])
def auth_signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("auth/signupSelect.html")

@app.route("/auth/signup/student/", methods=["GET", "POST"])
def auth_signupStudent():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("auth/signup.html", form = SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signup.html", form = form, error = "Remember to fill all the fields.")

    u = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
    r = Role.query.filter_by(name="STUDENT").first()
    u.roles.append(r)

    db.session.add(u)
    db.session.commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/signup/teacher/", methods=["GET", "POST"])
def auth_signupTeacher():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("auth/teacherSignup.html", form = SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/teacherSignup.html", form = form, error = "Remember to fill all the fields.")

    u = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
    r = Role.query.filter_by(name="TEACHER").first()
    u.roles.append(r)

    db.session.add(u)
    db.session.commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/logout/")
def auth_logout():
    app.jinja_env.globals.update(is_student=False)
    app.jinja_env.globals.update(is_teacher=False)

    logout_user()
    return redirect(url_for("index"))
