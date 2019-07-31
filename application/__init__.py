from flask import Flask
app = Flask(__name__)

# Database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///logs.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# from jinja2 import Environment, FileSystemLoader

# env = Environment(loader = FileSystemLoader('application'), keep_trailing_newline=True)

from application import views

from application.logs import models
from application.logs import views

from application.auth import models
from application.auth import views

# Login
from application.auth.models import Student
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_studentLogin"
login_manager.login_message = "Please login to use this feature"

@login_manager.user_loader
def load_student(student_id):
    return Student.query.get(student_id)

# Create database tables if they don't exist
try:
    db.create_all()
except:
    pass
