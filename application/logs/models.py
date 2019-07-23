from application import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    duration = db.Column(db.Float,  nullable=False)

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
