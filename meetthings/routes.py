from flask import (
    render_template,
    flash,
    redirect,
    request,
    url_for,
)
from meetthings import app
from meetthings.forms import NewMeetupEvent


@app.route('/')
@app.route('/index')
def index():
    return "Hi"


@app.route('/NewEvent', methods=['GET', 'POST'])
def create_event():
    form = NewMeetupEvent(request.form)
    if request.method == "POST":
        # I have to create the event here or something..??
        flash("New event created!")
        return redirect(url_for('index'))

    form.group_id.data = app.config['GROUP_ID']
    form.group_urlname.data = app.config['URLNAME']
    form.venue_id.data = app.config['VENUE_ID']

    form.anncounce = False  # Everything passing here will not be annouced
    form.publish_status = False  # Everything passing here is in draft
    return render_template('create_event.html', title="new event", form=form)
