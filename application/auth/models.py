from application import db

class Student(db.Model):
    __tablename__: "student"

    studentId = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144))

    def __init__(self, studentId, firstname, lastname, email, password):
        self.studentId = studentId
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def get_id(self):
        return self.studentId

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
