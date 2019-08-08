from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/login.html", form = form, error = "Remember to fill all the fields")

    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()

    if not user:
        return render_template("auth/login.html", form = form, error = "Incorrect email address or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout/")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup/", methods=["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signup.html", form = SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signup.html", form = form, error = "Remember to fill all the fields.")

    u = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)

    db.session.add(u)
    db.session.commit()

    return redirect(url_for("auth_login"))
