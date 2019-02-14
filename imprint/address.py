from flask import current_app as app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

bp = Blueprint('address', __name__)

GoogleMaps(app)

@bp.route('/address')
def generateMap():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    return render_template('address/address.html', mymap=mymap)