from application import app, db
from application.models import Base
from datetime import datetime
from flask_login import current_user
from sqlalchemy.sql import text

user_course = db.Table("usercourse",
    db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id", ondelete="CASCADE")))

class Course(Base):

    course_id = db.Column(db.String(144), nullable=True)
    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144),  nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)

    logs = db.relationship("Log", backref="course", lazy=True)

    users = db.relationship("User", secondary=user_course, backref = db.backref("courses", lazy="dynamic", passive_deletes=True))

    def __init__(self, course_id, title, description, duration, deadline):
        self.course_id = course_id
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
        statement = text("SELECT Course.id, Course.course_id, Course.title, Course.description, Course.duration, Course.deadline, COUNT(Usercourse.user_id)-1 AS Students FROM Course "
                        "LEFT JOIN Usercourse ON Course.id = Usercourse.course_id "
                        "GROUP BY Course.id;")
        result = db.engine.execute(statement)

        response = []

        for row in result:
            if Course.is_local():
                # Format datetime object
                date = Course.datetime_format(row[5])
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "description":row[3], "duration":row[4], "deadline":Course.date_format(date), "students":row[6]})
            else:
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "description":row[3], "duration":row[4], "deadline":row[5], "students":row[6]})

        return response

    @staticmethod
    def count_enrolled_students_in_each_course_with_search_term(search_term):
        search_term = '%' + search_term + '%'

        statement = text("SELECT Course.id, Course.course_id, Course.title, Course.description, Course.duration, Course.deadline, COUNT(Usercourse.user_id)-1 AS Students FROM Course "
                        "LEFT JOIN Usercourse ON Course.id = Usercourse.course_id "
                        "WHERE Course.course_id LIKE :search_term OR Course.title LIKE :search_term "
                        "GROUP BY Course.id;").params(search_term=search_term)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            if Course.is_local():
                # Format datetime object
                date = Course.datetime_format(row[5])
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "description":row[3], "duration":row[4], "deadline":Course.date_format(date), "students":row[6]})
            else:
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "description":row[3], "duration":row[4], "deadline":row[5], "students":row[6]})

        return response

    @staticmethod
    def fetch_five_most_recent_courses():
        if Course.is_local():
            statement = text("SELECT Course.id, Course.course_id, Course.title, Course.description, Course.duration, Course.deadline FROM Course "
                            "LEFT JOIN Usercourse ON Course.id = Usercourse.course_id "
                            "WHERE Usercourse.user_id = :id "
                            "GROUP BY Course.id "
                            "ORDER BY Course.date_created DESC, Course.date_modified DESC "
                            "LIMIT 5;").params(id=current_user.id)
        else:
            statement = text("SELECT Course.id, Course.course_id, Course.title, Course.description, Course.duration, Course.deadline FROM Course "
                            "LEFT JOIN Usercourse ON Course.id = Usercourse.course_id "
                            "WHERE Usercourse.user_id = :id "
                            "GROUP BY Course.id "
                            "ORDER BY Course.date_created DESC, Course.date_modified DESC "
                            "FETCH FIRST 5 ROWS ONLY;").params(id=current_user.id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            response.append({"id":row[0], "course_id":row[1], "title":row[2]})

        return response

    @staticmethod
    def fetch_users_courses_without_logs():
        statement = text("SELECT Course.id, Course.course_id, Course.title, Course.deadline FROM Usercourse "
                        "LEFT JOIN Course ON Usercourse.course_id = Course.id "
                        "WHERE Usercourse.user_id = :id AND "
                        "Course.id NOT IN "
                        "(SELECT Log.course_id FROM Log "
                        "WHERE Log.user_id = :id);").params(id=current_user.id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            # Format datetime object
            if Course.is_local():
                date = Course.datetime_format(row[3])
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "deadline":Course.date_format(date)})
            else:
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "deadline":row[3]})

        return response

    # Helper functions
    @staticmethod
    def is_local():
        if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
            return True
        return False

    @staticmethod
    def datetime_format(date):
        date = date.split(" ")
        date[-1] = date[-1][:8]
        date = " ".join(date)
        return date

    @staticmethod
    def date_format(date):
        return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
