from os import environ

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("config/base_setting.py")
if "ops_config" in environ:
    app.config.from_pyfile("config/{}_setting.py".format(environ["ops_config"]))

db = SQLAlchemy(app)

manager = Manager(app)
