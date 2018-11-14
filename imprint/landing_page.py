from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from imprint.db import get_db
from imprint.auth import login_required
from slugify import slugify # generates URL slug
from werkzeug.utils import secure_filename
from flask import current_app as app
import os
import pdb

bp = Blueprint('landing_page', __name__)

""" """"""""""""""""""ADDING LANDING PAGE"""""""""""""""""" """

@bp.route('/add-landing-page', methods=('GET','POST'))
def add_landing_page():
    if request.method == 'POST':
        db = get_db()

        heading = request.form['heading']
        subheading = request.form['subheading']
        button_text = request.form['button-text']

        error = None

        if not heading:
            error = "A 'Heading' is required"
        elif not subheading:
            error = "A 'Subheading' is required"
        elif not button_text:
            error = "Button Text is required"

        if error is not None:
            flash(error)
        else:
            url = slugify(heading)
            db.execute("INSERT INTO landing (heading, subheading, button_text, author_id, url) VALUES (?,?,?,?,?)",(heading,subheading,button_text,g.user['id'], url))
            db.commit()

            return redirect(url_for('landing_page.new_landing_page',slug=url))

    return render_template('page/add_landing_page.html')

def get_landing_page(slug):
    landing_page = get_db().execute('SELECT heading, subheading, button_text FROM landing WHERE url=?',(slug,)).fetchone()

    if landing_page is None:
        abort(404, "URL {0} doesn't exist. [landing]".format(slug))

    return landing_page

@bp.route('/<slug>',methods=('GET','POST'))
def new_landing_page(slug):
    landing_page = get_landing_page(slug)
    return render_template('page/landing-page.html', landing_page=landing_page)
