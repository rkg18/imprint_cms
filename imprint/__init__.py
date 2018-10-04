# __init__.py

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Database connection

""" Creates and Configures Application """
def create_app(test_config=None):
    # Creates Instance & Tells App where files are relative
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return '<h1> Hello World </h1>'

    return app
