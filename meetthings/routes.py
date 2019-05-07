from flask import (
    render_template,
    flash,
    redirect,
    request,
    url_for,
)
from meetthings import app
from meetthings.util import load_schema
from meetthings.form_factory import form_factory


@app.route('/')
@app.route('/index')
def index():
    return "Hi"


@app.route('/NewEvent', methods=['GET', 'POST'])
def create_event():
    if request.method == "POST":
        # I have to create the event here or something..??
        flash("New event created!")
        return redirect(url_for('index'))

    form_classes = form_factory(load_schema('meetthings'))
    forms = {name: form() for name, form in form_classes.items()}

    import pudb
    pudb.set_trace()
    # form.group_id.data = app.config['GROUP_ID']
    # form.group_urlname.data = app.config['URLNAME']
    # form.venue_id.data = app.config['VENUE_ID']

    # form.anncounce = False  # Everything passing here will not be annouced
    # form.publish_status = False  # Everything passing here is in draft
    return render_template('create_event.html', title="new event", forms=forms)
