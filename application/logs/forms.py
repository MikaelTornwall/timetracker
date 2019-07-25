from flask_wtf import FlaskForm
from wtforms import TextAreaField, DecimalField, validators
from wtforms.ext.csrf.session import SessionSecureForm

class LogForm(FlaskForm):
    description = TextAreaField("Description", [validators.Length(min=3)])
    duration = DecimalField("Duration (h)", [validators.DataRequired(), validators.NumberRange(min=0, max=24, message="You can only add numbers from 0 to 24")])

    class Meta:
        csrf=False
