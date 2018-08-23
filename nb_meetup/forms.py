from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired


class NewMeetupEvent(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    duration =
