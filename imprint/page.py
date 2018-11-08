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
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

bp = Blueprint('page', __name__)

@bp.route('/add-page', methods=('GET','POST'))
def add_page():
    if request.method == 'POST':
        pageType = request.form.get('page-types')

        db = get_db()
        if pageType == 'landing-page':
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
                db.execute("INSERT INTO landing_pages (heading, subheading, button_text, author_id, url) VALUES (?,?,?,?,?)",(heading,subheading,button_text,g.user['id'], url))
                db.commit()

                return redirect(url_for('page.new_page',slug=url, pageType=pageType))

        elif pageType == 'product-page':
            product_title = request.form['product-title']
            product_description = request.form['product-description']

            """ Grabs image from form """
            if 'new_file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            new_file = request.files['new_file']

            if new_file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if new_file and allowed_file(new_file.filename):
                filename = secure_filename(new_file.filename)
                new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                url = slugify(product_title)
                db.execute("INSERT INTO product_pages (title, description, filename, author_id, url) VALUES (?,?,?,?,?)",(product_title,product_description,filename,g.user['id'], url))
                db.commit()
                return redirect(url_for('page.new_page',slug=url, pageType=pageType))
    else:
        return render_template('page/add_page.html')

# Determines if there is a valid file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_page(slug, sql):
    page = get_db().execute(sql).fetchone()

    if page is None:
        abourt(404, "URL {0} doesn't exist.".format(slug))

@bp.route('/<pageType>/<slug>',methods=('GET','POST'))
def new_page(slug, pageType):

    if pageType == 'product-page':
        sql = 'SELECT title, description, filename FROM product_pages WHERE url={0}'.format(slug)
        page = get_page(slug, sql)
        return render_template('page/product-page.html', page=page)
    elif pageType == 'landing-page':
        sql = 'SELECT heading, subheading, button_text FROM landing_pages WHERE url={0}'.format(slug)
        page = get_page(slug,sql)
        return render_template('page/landing-page.html', page=page)

"""
def get_landing_page(slug):
    landing_page = get_db().execute('SELECT heading, subheading, button_text FROM landing_pages WHERE url=?',(slug,)).fetchone()

    if landing_page is None:
        abort(404, "URL {0} doesn't exist.".format(slug))

    return landing_page

@bp.route('/<slug>',methods=('GET','POST'))
def new_landing_page(slug):
    landing_page = get_landing_page(slug)
    return render_template('page/landing-page.html', page=landing_page)

def get_product_page(slug):
    product_page = get_db().execute('SELECT title, description, filename FROM product_pages WHERE url=?',(slug,)).fetchone()

    if product_page is None:
        abort(404, "URL {0} doesn't exist.".format(slug))

    return product_page

@bp.route('/<slug>',methods=('GET','POST'))
def create_product_page(slug):
    product_page = get_product_page(slug)
    return render_template('page/product-page.html', page=product_page)
"""
