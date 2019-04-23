from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('APPLICATION_SETTINGS')

from meetthings import routes  # NOQA
