from application import app, db
from application.models import Base
from datetime import datetime
from flask_login import current_user
from sqlalchemy.sql import text

user_course = db.Table("usercourse",
    db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id", ondelete="CASCADE")))

class Course(Base):

    courseId = db.Column(db.String(144), nullable=True)
    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144),  nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)

    logs = db.relationship("Log", backref="course", lazy=True)

    users = db.relationship("User", secondary=user_course, backref = db.backref("courses", lazy="dynamic", passive_deletes=True))

    def __init__(self, courseId, title, description, duration, deadline):
        self.courseId = courseId
        self.title = title
        self.description = description
        self.duration = duration
        self.deadline = deadline

    @staticmethod
    def count_courses():
        statement = text("SELECT COUNT(*) FROM Course;")
        result = db.engine.execute(statement)

        return result.fetchall()[0][0]

    @staticmethod
    def find_students(course_id):
        statement = text("SELECT * FROM Account "
                        "LEFT JOIN Userrole ON Userrole.user_id = Account.id "
                        "LEFT JOIN Role ON Role.id = Userrole.role_id "
                        "LEFT JOIN Usercourse ON Usercourse.user_id = Account.id "
                        "LEFT JOIN Course ON Course.id = Usercourse.course_id "
                        "WHERE Course.id = :id AND Role.name = 'STUDENT' "
                        "ORDER BY Account.firstname, Account.lastname;").params(id=course_id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            response.append({"id":row[0], "firstname":row[3], "lastname":row[4]})

        return response

    @staticmethod
    def count_students(course_id):
        statement = text("SELECT COUNT(*) FROM Account "
                        "LEFT JOIN Userrole ON Userrole.user_id = Account.id "
                        "LEFT JOIN Role ON Role.id = Userrole.role_id "
                        "LEFT JOIN Usercourse ON Usercourse.user_id = Account.id "
                        "LEFT JOIN Course ON Course.id = Usercourse.course_id "
                        "WHERE Course.id = :id AND Role.name = 'STUDENT';").params(id=course_id)
        result = db.engine.execute(statement)

        return result.fetchall()[0][0]

    @staticmethod
    def count_enrolled_students_in_each_course():
        statement = text("SELECT Course.id, Course.courseId, Course.title, Course.description, Course.duration, Course.deadline, COUNT(Usercourse.user_id)-1 AS Students FROM Course "
                        "LEFT JOIN Usercourse ON Course.id = Usercourse.course_id "
                        #"LEFT JOIN Account ON Usercourse.user_id = Account.id "
                        #"LEFT JOIN Userrole ON Account.id = Userrole.user_id "
                        #"LEFT JOIN ROLE ON Userrole.role_id = Role.id "
                        "GROUP BY Course.id;")

        result = db.engine.execute(statement)

        response = []

        for row in result:
            if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
                # Format datetime object
                date = row[5]
                date = date.split(" ")
                date[-1] = date[-1][:8]
                date = " ".join(date)
                response.append({"id":row[0], "courseId":row[1], "title":row[2], "description":row[3], "duration":row[4], "deadline":datetime.strptime(date, '%Y-%m-%d %H:%M:%S'), "students":row[6]})
            else:
                response.append({"id":row[0], "title":row[1], "description":row[2], "duration":row[3], "deadline":row[4], "students":row[5]})

        print("RESPONSE:")
        print(response)

        return response
