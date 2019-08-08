from application import db
from application.models import Base

class Course(Base):
    __tablename__: "course"

    courseId = db.Column(db.String(144), nullable=True)
    title = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144),  nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)

    logs = db.relationship("Log", backref="course", lazy=True)
    # Many-to-many -suhde käyttäjään

    def __init__(self, courseId, title, description, duration, deadline):
        self.courseId = courseId
        self.title = title
        self.description = description
        self.duration = duration
        self.deadline = deadline
