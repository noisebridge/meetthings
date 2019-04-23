from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    BooleanField,
    SelectField,
    SubmitField,
)
from wtforms.ext.dateutil.fields import DateTimeField

from wtforms.validators import (
    DataRequired,
    NumberRange,
)
from meetthings.validators import (
    length,
    isValidValue,
)
from meetthings.models import Venue, Event
from meetthings import app
from meetthings import choices


class NewMeetupEvent(FlaskForm):
    announce = SelectField("Announce Meetup: ",
                           choices=[(1, "No"), (2, "Yes")],
                           default=1)
    name = StringField('Event name', validators=[DataRequired(), length(80)])
    description = StringField('description',
                              validators=[length(0, 50000, "description limited to 50,000 characters")])  # NOQA
    simple_html_description = StringField('simple html desc')
    event_hosts = StringField('host ids')
    email_reminders = BooleanField('reminders')
    featured_photo_id = IntegerField("Photo id")

    group_id = IntegerField('group id')
    group_urlname = StringField('group url')

    guest_limit = IntegerField('guest limit')
    host_instructions = StringField('host instructions')
    how_to_find_us = StringField("How to find us")
    publish_status = BooleanField('publish status')
    questions = StringField("questions")

    rsvp_alerts = BooleanField('rsvp alerts')
    rsvp_close = IntegerField('rsvp close time', default=1)
    rsvp_limit = IntegerField('max rsvps', default=0)
    rsvp_open = IntegerField('rsvp start time', default=0)
    self_rsvp = BooleanField("self_rsvp", default=True)

    time = DateTimeField('start time')
    duration = IntegerField('duration (mins)',
                            validators=[NumberRange(min=0)],
                            default=90)
    start_day = SelectField('Day',
                            validators=[isValidValue(1, 31)],
                            choices=choices.DAYS
                            )
    start_month = SelectField("Month",
                              validators=[isValidValue(1, 12)],
                              choices=choices.MONTHS)
    start_year = SelectField("Year",
                             choices=choices.YEARS)
    start_hour = SelectField("Hour",
                             validators=[isValidValue(1, 12)],
                             choices=choices.HOURS)
    start_min = SelectField("Min",
                            validators=[isValidValue(0, 59)],
                            choices=choices.MINS)
    start_day_part = SelectField("AM/PM",
                                 validators=[isValidValue(0, 1)],
                                 choices=[(0, "AM"), (1, "PM")])
    end_day = SelectField('Day',
                          validators=[isValidValue(1, 31)],
                          choices=choices.DAYS
                          )
    end_month = SelectField("Month",
                            validators=[isValidValue(1, 12)],
                            choices=choices.MONTHS)
    end_year = SelectField("Year",
                           choices=choices.YEARS)
    end_hour = SelectField("Hour",
                           validators=[isValidValue(1, 12)],
                           choices=choices.HOURS)
    end_min = SelectField("Min",
                          validators=[isValidValue(0, 59)],
                          choices=choices.MINS)
    end_day_part = SelectField("AM/PM",
                               validators=[isValidValue(0, 1)],
                               choices=[(0, "AM"), (1, "PM")])

    venue_id = IntegerField('venue id',
                            validators=[DataRequired()])
    venue_visibility = StringField('venue visibility')
    venue = Venue
#     nb = Noisebridge
    submit = SubmitField("Create Event!")

    def validate_description(form, field):
        if len(field.data) > 50000:
            raise ValidationError('Description can only be 50k characters')
