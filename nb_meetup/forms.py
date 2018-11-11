from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired
from nb_meetup import app


class NewMeetupEvent(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    duration = IntegerField('duration')
    email_reminders = BooleanField('reminders')
    group_id = IntegerField('group id')
    group_urlname = StringField('group url',
                                default=app.config['GROUP_URLNAME'])
    guest_limit = IntegerField('guests')
    host_instructions = StringField('hst instructions')
    hosts = StringField('host ids')
    how_to_find_us = StringField('how to find')
    name = StringField('event name')
    publish_status = StringField('publish status')
    questions = StringField("questions")
    rsvp_alerts = BooleanField('rsvp alerts')
    rsvp_close = IntegerField('rsvp close time')
    rsvp_limit = IntegerField('max rsvps')
    rsvp_open = IntegerField('rsvp start time')
    simple_html_description = StringField('simple html desc')
    time = IntegerField('start time')
    venue_id = IntegerField('venue id')
    venue_visibility = StringField('venue visibility')
    waitlisting = StringField('waitlist status')
    why = StringField('why')

    def validate_description(form, field):
        if len(field.data) > 50000:
            raise ValidationError('Description can only be 50k characters')
