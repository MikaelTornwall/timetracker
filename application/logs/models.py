from application import db
from application.models import Base

from datetime import datetime

from sqlalchemy.sql import text

class Log(Base):
    __tablename__: "log"

    description = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Float,  nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False)

    def __init__(self, description, duration):
        self.description = description
        self.duration = duration

    @staticmethod
    def find_logs_of_course(course_id, user_id):
        statement = text("SELECT * FROM Log "
                        "WHERE Log.course_id = :courseId AND Log.user_id = :userId;").params(courseId=course_id, userId=user_id)

        result = db.engine.execute(statement)

        response = []

        for row in result:
            response.append({"id":row[0], "date":datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), "description":row[3], "duration":row[4]})

        print("RESPONSE")
        print(response)
        return response

    @staticmethod
    def total_workhours(course_id, user_id):
        statement = text("SELECT SUM(duration) FROM Log "
                         "WHERE Log.course_id = :courseId AND Log.user_id = :userId;").params(courseId=course_id, userId=user_id)

        result = db.engine.execute(statement)

        response = result.fetchall()[0][0]

        print("RESPONSE")
        print(response)
        return response
