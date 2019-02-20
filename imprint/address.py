from flask import current_app as app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from imprint.db import get_db
from geopy.geocoders import Nominatim

bp = Blueprint('address', __name__)

GoogleMaps(app)

# Default Address for Menu Item 'Address'
@bp.route('/address',methods=('GET','POST'))
def indexMap():
    mapVal = get_address()

    geolocator = Nominatim()
    full_address = "{} {} {}".format(mapVal['street'],mapVal['city'],mapVal['state'])
    gc = geolocator.geocode(full_address)
    print(gc.latitude)
    print(gc.longitude)

    return render_template('address/address.html', lat=gc.latitude, long=gc.longitude)

# Add New Address to Geolocation
@bp.route('/add-address', methods=('GET','POST'))
def add_address():
    if request.method == 'POST':
        city = request.form['city']
        street = request.form['street']
        state = request.form['state']

        error = None

        if not street:
            error = "City is required"
        elif not street:
            error = "Street is required"
        elif not state:
            error = "State is required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute("INSERT INTO locations (street, city, state, author_id) VALUES (?, ?, ?, ?)", (street,city,state, g.user['id']))
            db.commit()

            return redirect(url_for('address.indexMap'))

    return render_template('address/add_address.html')

def get_address():
    db = get_db()

    ad = get_db().execute('SELECT city, state, street FROM locations WHERE author_id=?',(g.user['id'],)).fetchone()

    return ad
