from application import db

class Log(db.Model):
    __tablename__: "log"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    description = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Float,  nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.studentId'), nullable = False)

    def __init__(self, description, duration):
        self.description = description
        self.duration = duration
