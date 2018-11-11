from flask import render_template
from nb_meetup import app
from nb_meetup.forms import NewMeetupEvent


@app.route('/')
@app.route('/index')
def index():
    return "Hi"


@app.route('/NewEvent')
def create_event():
    form = NewMeetupEvent()
    return render_template('create_event.html', title="new event", form=form)
