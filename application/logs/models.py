from application import app, db
from application.models import Base
from flask_login import current_user
from datetime import datetime
from sqlalchemy.sql import text

class Log(Base):

    description = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Float,  nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False)

    def __init__(self, description, duration):
        self.description = description
        self.duration = duration

    @staticmethod
    def find_logs_of_course(course_id, user_id):
        statement = text("SELECT * FROM Log "
                        "WHERE Log.course_id = :course_id AND Log.user_id = :user_id "
                        "ORDER BY Log.date_created ASC;").params(course_id=course_id, user_id=user_id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            if Log.is_local():
                response.append({"id":row[0], "date":Log.date_format(row[1]), "description":row[3], "duration":row[4]})
            else:
                response.append({"id":row[0], "date":row[1], "description":row[3], "duration":row[4]})

        return response

    @staticmethod
    def find_logs_of_course_desc(course_id, user_id):
        statement = text("SELECT * FROM Log "
                        "WHERE Log.course_id = :course_id AND Log.user_id = :user_id "
                        "ORDER BY Log.date_created DESC;").params(course_id=course_id, user_id=user_id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            if Log.is_local():
                response.append({"id":row[0], "date":Log.date_format(row[1]), "description":row[3], "duration":row[4]})
            else:
                response.append({"id":row[0], "date":row[1], "description":row[3], "duration":row[4]})

        return response

    @staticmethod
    def total_workhours(course_id, user_id):
        statement = text("SELECT SUM(duration) FROM Log "
                         "WHERE Log.course_id = :course_id AND Log.user_id = :user_id;").params(course_id=course_id, user_id=user_id)
        result = db.engine.execute(statement)

        response = result.fetchall()[0][0]

        return response

    @staticmethod
    def fetch_five_most_recent_courses_with_activity():
        if Log.is_local():
            statement = text("SELECT Course.id, Course.course_id, Course.title, COUNT(*) FROM Log "
                            "JOIN Course ON Log.course_id = Course.id "
                            "GROUP BY Course.id "
                            "HAVING Log.user_id = :id "
                            "ORDER BY Log.date_created DESC, Log.date_modified DESC "
                            "LIMIT 5;").params(id=current_user.id)
        else:
            statement = text("SELECT Course.id, Course.course_id, Course.title, COUNT(*) FROM "
                            "(SELECT * FROM Log "
                            "WHERE Log.user_id = :id "
                            "ORDER BY Log.date_created DESC, Log.date_modified DESC) AS L "
                            "JOIN Course ON L.course_id = Course.id "
                            "GROUP BY Course.id "
                            "ORDER BY MAX(L.date_created) DESC, MAX(L.date_modified) DESC "
                            "FETCH FIRST 5 ROWS ONLY;").params(id=current_user.id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            response.append({"id":row[0], "course_id":row[1], "title":row[2], "logs":row[3]})

        return response

    @staticmethod
    def fetch_students_courses_with_progress():
        statement = text("SELECT Course.id, Course.course_id, Course.title, Course.duration, Course.deadline, SUM(Log.duration) as progress FROM Log "
                        "LEFT JOIN Course ON Log.course_id = Course.id "
                        "WHERE Log.user_id = :id "
                        "GROUP BY Course.id;"
                        ).params(id=current_user.id)
        result = db.engine.execute(statement)

        response = []

        for row in result:
            if row[5] == None:
                progress = 0
            else:
                progress = row[5]

            if Log.is_local():
                # Format datetime object
                date = Log.datetime_format(row[4])
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "duration":row[3], "deadline":Log.date_format(date), "progress":progress})
            else:
                response.append({"id":row[0], "course_id":row[1], "title":row[2], "duration":row[3], "deadline":row[4], "progress":progress})

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
