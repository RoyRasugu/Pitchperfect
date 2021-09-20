from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, TextAreaField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
