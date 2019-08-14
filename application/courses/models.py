from application import db
from application.models import Base

from sqlalchemy.sql import text

user_course = db.Table("usercourse",
    db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id", ondelete="CASCADE")))

class Course(Base):
    __tablename__: "course"

    logs = db.relationship("Log", backref="course", lazy=True)

    # Many-to-many -suhde käyttäjään
    #users = db.relationship("User", secondary="usercourse")
    users = db.relationship("User", secondary=user_course, backref = db.backref("courses", lazy="dynamic", passive_deletes=True))

    courseId = db.Column(db.String(144), nullable=True)
    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144),  nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)

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
                        "WHERE Course.id = :id AND Role.name = 'STUDENT'").params(id=course_id)
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
                        "WHERE Course.id = :id AND Role.name = 'STUDENT'").params(id=course_id)
        result = db.engine.execute(statement)

        return result.fetchall()[0][0]

    def countStudents():
        return
