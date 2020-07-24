"""
www.py

Register blueprints
"""
from flask_debugtoolbar import DebugToolbarExtension

from application import app
from controllers.index import index

toolbar = DebugToolbarExtension(app)


def register():
    app.register_blueprint(index, url_prefix="/")
    pass
