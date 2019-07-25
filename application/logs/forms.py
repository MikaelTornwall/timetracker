from flask_wtf import FlaskForm
from wtforms import TextAreaField, DecimalField, validators
from wtforms.ext.csrf.session import SessionSecureForm

class LogForm(FlaskForm):
    description = TextAreaField("Description", [validators.Length(min=3)])
    duration = DecimalField("Duration (h)", [validators.DataRequired()])

    class Meta:
        csrf=False
