from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from imprint.db import get_db
from imprint.auth import login_required
from slugify import slugify # generates URL slug

bp = Blueprint('landing_page', __name__)

@bp.route('/landing-page')
def landing_index():
    pages = get_db().execute('SELECT url, heading, author_id FROM landing').fetchall()

    return render_template('page/landing_page.html', pages=pages)

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
    landing_page = get_db().execute('SELECT page_id, heading, subheading, button_text, url, author_id FROM landing WHERE url=?',(slug,)).fetchone()

    if landing_page is None:
        abort(404, "URL {0} doesn't exist. [landing]".format(slug))

    return landing_page


""" Edit feature """
@bp.route('/landing-page/<slug>/edit', methods=('GET', 'POST'))
@login_required
def edit_landing_page(slug):
    page = get_landing_page(slug)

    if request.method == 'POST':
        heading = request.form['heading']
        subheading = request.form['subheading']
        button_text = request.form['button-text']
        error = None

        newUrl = slugify(heading)

        if not heading:
            error = 'A heading is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE landing SET heading = ?, subheading = ?, button_text = ? WHERE url = ?',(heading,subheading,button_text, slug))
            db.commit()
            return redirect(url_for('landing_page.new_landing_page', slug=slug))

    return render_template('page/edit_landing_page.html', landing_page=page)

@bp.route('/landing-page/<slug>',methods=('GET','POST'))
def new_landing_page(slug):
    landing_page = get_landing_page(slug)
    return render_template('page/landing-page.html', landing_page=landing_page)
