from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, validators

class LoginForm(FlaskForm):
    email = StringField("Email address", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired()])

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    studentId = IntegerField("Student ID", [validators.DataRequired(), validators.NumberRange(min=1, max=9999999999, message="Student ID should contain only numbers. Maximum length is 10 characters.")])
    firstname = StringField("Firstname", [validators.DataRequired(), validators.Length(min=2)])
    lastname = StringField("Lastname", [validators.DataRequired(), validators.Length(min=2)])
    email = StringField("Email", [validators.DataRequired(), validators.Email(), validators.Length(min=5)])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=8)])

    class Meta:
        csrf = False
