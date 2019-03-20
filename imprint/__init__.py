# __init__.py

import os

from flask import Flask
from flask import render_template
from flask_googlemaps import GoogleMaps
from imprint.config import *
from geocoder import *
from geopy.geocoders import Nominatim

UPLOAD_FOLDER = os.getcwd() + '/imprint/static/'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

""" Creates and Configures Application """
def create_app(test_config=None):
    # Creates Instance & Tells App where files are relative
    app = Flask(__name__, instance_relative_config=True)

    """ Sets configuration for DB with SQLITE3 """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'imprint.sqlite')
    )

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Sets configuration for images

    # config for google maps
    app.config['GOOGLEMAPS_KEY'] = config.mapsKey
    GoogleMaps(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return  render_template('index.html')

    @app.route('/website')
    def website_index():
        return render_template('index.html')

    """ Adding Database to 'app' """
    from . import db
    db.init_app(app)

    """ Adding Authroization to 'app'"""
    from . import auth
    app.register_blueprint(auth.bp)

    """ Adding admin dashboard panel """
    from . import dashboard
    app.register_blueprint(dashboard.bp)

    """ Adding blog """
    from . import blog
    app.register_blueprint(blog.bp)

    """ Adding Pages"""
    from . import product_page
    app.register_blueprint(product_page.bp)

    """ Add Landing Page"""
    from . import landing_page
    app.register_blueprint(landing_page.bp)

    """ ADdress """
    from . import address
    app.register_blueprint(address.bp)

    """ Live Site """
    from . import live
    app.register_blueprint(live.bp)

    return app
