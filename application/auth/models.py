from application import db
from application.models import Base

user_role = db.Table("userrole",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")))

class Role(Base):
    name = db.Column(db.String(32), nullable=False, unique=True)
    superuser = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    def init(self, name, superuser):
        name = self.name
        superuser = self.superuser

class User(Base):
    __tablename__: "user"

    #studentId = db.Column(db.Integer, primary_key=True, unique=True)

    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144))

    logs = db.relationship("Log", backref="user", lazy=True)
    #courses = db.relationship("Course", backref="user", passive_deletes=True, lazy=True)
    # Many-to-many suhde opiskelijoiden ja kurssien välille
    # courses = db.relationship("Course", backref="student", lazy=True)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

"""
class Teacher(Base):
    __tablename__: "teacher"

    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144))

    # logs = db.relationship("Log", backref="teacher", lazy=True)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class Student(Base):
    __tablename__: "student"

    #studentId = db.Column(db.Integer, primary_key=True, unique=True)

    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144))

    logs = db.relationship("Log", backref="student", lazy=True)
    # Many-to-many suhde opiskelijoiden ja kurssien välille
    # courses = db.relationship("Course", backref="student", lazy=True)

    def __init__(self, firstname, lastname, email, password):
        #self.studentId = studentId
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
"""
