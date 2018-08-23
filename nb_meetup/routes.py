from nb_meetup import app

@app.route('/')
@app.route('/index')
def index():
    return "Hi"
