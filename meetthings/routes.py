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
        flash("New event created!")
        return redirect(url_for('index'))

    form_classes = form_factory(load_schema('meetthings'))
    forms = {name: form() for name, form in form_classes.items()}

    return render_template('create_event.html', title="new event", forms=forms)
