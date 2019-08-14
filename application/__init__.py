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

# Login
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this feature"

# roles in login_required
from functools import wraps

def is_student():
    if current_user:
        student = current_user.is_student()
        teacher = current_user.is_teacher()
        app.jinja_env.globals.update(is_student=student)
        app.jinja_env.globals.update(is_teacher=teacher)
        return
    else:
        app.jinja_env.globals.update(is_student=False)
        app.jinja_env.globals.update(is_teacher=False)
        return

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.get_roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

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

@event.listens_for(Role.__table__, 'after_create')
def insert_initial_roles(*args, **kwargs):
    db.session.add(Role("TEACHER", True))
    db.session.add(Role("STUDENT", False))
    db.session.commit()

from application.auth.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create database tables if they don't exist
try:
    db.create_all()
    insert_initial_roles()
except:
    pass
