from flask import Flask
from meetup_config import Config


app = Flask(__name__)
app.config.from_object(Config)

from nb_meetup import routes  # NOQA
