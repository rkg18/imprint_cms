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

    return render_template('landing_page/landing_page_index.html', pages=pages)

""" """"""""""""""""""ADDING LANDING PAGE"""""""""""""""""" """

@bp.route('/add-landing-page', methods=('GET','POST'))
def add_landing_page():
    if request.method == 'POST':
        db = get_db()

        heading = request.form['heading']
        subheading = request.form['subheading']
        button_text = request.form['button-text']
        button_url = request.form['button-url']

        email_cta = request.form.get('signup')
        info_header = request.form.get('info-header')
        info_block = request.form.get('info-block')

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
            db.execute("INSERT INTO landing (heading, subheading, button_text, button_url, author_id, url, email_cta, info_header, info_block) VALUES (?,?,?,?,?,?,?,?,?)",(heading,subheading,button_text,button_url,g.user['id'], url, email_cta, info_header, info_block))
            db.commit()

            return redirect(url_for('landing_page.new_landing_page',slug=url))

    return render_template('landing_page/add_landing_page.html')

def get_landing_page(slug):
    landing_page = get_db().execute('SELECT page_id, heading, subheading, button_text, button_url, url, author_id, email_cta, info_header, info_block FROM landing WHERE url=?',(slug,)).fetchone()

    if landing_page is None:
        abort(404, "URL {0} doesn't exist. [landing]".format(slug))

    return landing_page


""" Edit feature """
@bp.route('/landing-page/<slug>/edit', methods=('GET', 'POST'))
@login_required
def edit_landing_page(slug):
    page = get_landing_page(slug)

    oldHeading = page['heading']

    if request.method == 'POST':
        heading = request.form['heading']
        subheading = request.form['subheading']
        button_text = request.form['button-text']
        button_url = request.form['button-url']
        error = None

        email_cta = request.form.get('signup')
        info_header = request.form.get('info-header')
        info_block = request.form.get('info-block')

        newUrl = slugify(heading)

        if not heading:
            error = 'A heading is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()

            if (oldHeading != heading):
                db.execute("INSERT INTO landing (heading, subheading, button_text, button_url, author_id, url, email_cta, info_header, info_block) VALUES (?,?,?,?,?,?,?,?,?)",(heading,subheading,button_text,button_url,g.user['id'], newUrl, email_cta, info_header, info_block))
                db.execute("DELETE FROM landing WHERE url=?",(slug,))
            else:
                db.execute('UPDATE landing SET subheading = ?, button_text = ?, button_url = ? WHERE url = ?',(subheading,button_text,button_url,newUrl))

            db.commit()

            return redirect(url_for('landing_page.new_landing_page',slug=newUrl))

    return render_template('landing_page/edit_landing_page.html', landing_page=page)

# DELETES Landing Page
@bp.route('/landing-page/<slug>/delete', methods=('POST',))
@login_required
def delete_page(slug):
    get_landing_page(slug)
    db = get_db()
    db.execute('DELETE FROM landing WHERE url = ?', (slug,))
    db.commit()
    return redirect(url_for('landing_page.landing_index'))

@bp.route('/landing-page/<slug>',methods=('GET','POST'))
def new_landing_page(slug):
    landing_page = get_landing_page(slug)
    return render_template('landing_page/landing_page_template.html', landing_page=landing_page)
