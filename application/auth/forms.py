from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    email = StringField("Email address", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired()])

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    studentId = StringField("Student ID", [validators.DataRequired(), validators.Length(min=5)])
    firstname = StringField("Firstname", [validators.DataRequired(), validators.Length(min=2)])
    lastname = StringField("Lastname", [validators.DataRequired(), validators.Length(min=2)])
    email = StringField("Email", [validators.DataRequired(), validators.Email(), validators.Length(min=5)])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=8)])

    class Meta:
        csrf = False
