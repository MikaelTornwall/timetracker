from application import db
from application.models import Base

class Log(Base):
    __tablename__: "log"

    description = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Float,  nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False)

    def __init__(self, description, duration):
        self.description = description
        self.duration = duration
