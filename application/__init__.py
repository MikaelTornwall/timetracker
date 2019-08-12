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

from application.courses import models
from application.courses import views

# SQLite foreign key and role default value initialization
from sqlalchemy import event
from sqlalchemy.engine import Engine
from application.auth.models import Role, User

#@event.listens_for(Engine, "connect")
#def set_sqlite_pragma(dbapi_connection, connection_record):
#    if (app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite")):
#        cursor = dbapi_connection.cursor()
#        cursor.execute("PRAGMA foreign_keys=ON")
#        cursor.close()

@event.listens_for(Role.__table__, 'after_create')
def insert_initial_roles(*args, **kwargs):
    db.session.add(Role("TEACHER", True))
    db.session.add(Role("STUDENT", False))
    db.session.commit()

# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this feature"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create database tables if they don't exist
try:
    db.create_all()
except:
    pass
