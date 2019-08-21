from application import app, db
from application.models import Base

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
                        "WHERE Log.course_id = :course_id AND Log.user_id = :user_id;").params(course_id=course_id, user_id=user_id)

        result = db.engine.execute(statement)

        response = []

        for row in result:
            if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
                response.append({"id":row[0], "date":datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), "description":row[3], "duration":row[4]})
            else:
                response.append({"id":row[0], "date":row[1], "description":row[3], "duration":row[4]})

        print("RESPONSE")
        print(response)
        return response

    @staticmethod
    def total_workhours(course_id, user_id):
        statement = text("SELECT SUM(duration) FROM Log "
                         "WHERE Log.course_id = :course_id AND Log.user_id = :user_id;").params(course_id=course_id, user_id=user_id)

        result = db.engine.execute(statement)

        response = result.fetchall()[0][0]

        print("RESPONSE")
        print(response)
        return response
