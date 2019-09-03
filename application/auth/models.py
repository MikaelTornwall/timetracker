from application import db
from application.models import Base
from application.courses.models import Course, user_course

from sqlalchemy.sql import text

user_role = db.Table("userrole",
    db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")))

class Role(Base):

    name = db.Column(db.String(32), nullable=False, unique=True)
    superuser = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    def __init__(self, name, superuser = False):
        self.name = name
        self.superuser = superuser

class User(Base):
    __tablename__ = "account"

    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144))

    logs = db.relationship("Log", backref="account", lazy=True)

    roles = db.relationship("Role", secondary=user_role, lazy="subquery",
    backref=db.backref("users", passive_deletes=True, lazy=True))

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

    def is_student(self):
        role_arr = self.roles
        for row in role_arr:
            if row.name == "STUDENT":
                return True
        return False

    def is_teacher(self):
        role_arr = self.roles
        for row in role_arr:
            if row.name == "TEACHER":
                return True
        return False

    def get_roles(self):
        role_arr = self.roles
        response = []
        for row in role_arr:
            response.append(row.name)
        return response

    def get_user_roles(self):
        statement = text("SELECT name FROM Role "
                        "LEFT JOIN Userrole ON Userrole.role_id = Role.id "
                        "LEFT JOIN Account ON Account.id = Userrole.user_id "
                        "WHERE :id = Account.id").params(id=self.id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            response.append(row[0])

        return response

    @staticmethod
    def count_users_courses(self):
        statement = text("SELECT COUNT(*) FROM Usercourse"
                        " WHERE Usercourse.user_id = :id;").params(id=self.id)
        result = db.engine.execute(statement)

        return result.fetchall()[0][0]
