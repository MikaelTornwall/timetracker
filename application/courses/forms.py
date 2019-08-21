from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, DateTimeField, validators
from wtforms.ext.csrf.session import SessionSecureForm

class CourseForm(FlaskForm):
    course_id = StringField("Course ID", [validators.DataRequired()])
    title = StringField("Title", [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
    duration = IntegerField("Duration (h)", [validators.DataRequired(message = "Total required workload of the course in hours.")])
    deadline = DateTimeField("Course ends (dd.mm.yyyy hh:mm)", format='%d.%m.%Y %H:%M')

    class Meta:
        csrf=False
