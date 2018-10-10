# __init__.py

import os

from flask import Flask
from flask import render_template

""" Creates and Configures Application """
def create_app(test_config=None):
    # Creates Instance & Tells App where files are relative
    app = Flask(__name__, instance_relative_config=True)

    """ Sets configuration for DB with SQLITE3 """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'imprint.sqlite')
    )

    # a simple page that says hello
    @app.route('/')
    def hello():
        return  render_template('index.html')

    """ Adding Database to 'app' """
    from . import db
    db.init_app(app)

    """ Adding Authroization to 'app'"""
    from . import auth
    app.register_blueprint(auth.bp)

    """ Adding admin dashboard panel """
    from . import dashboard
    app.register_blueprint(dashboard.bp)

    return app
