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

bp = Blueprint('product_page', __name__)

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

""" """"""""""""""""""ADDING Product PAGE"""""""""""""""""" """

@bp.route('/add-product-page', methods=('GET','POST'))
def add_product_page():
    db=get_db()

    if request.method == "POST":
        product_title = request.form['product-title']
        product_description = request.form['product-description']

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
            db.execute("INSERT INTO product (title, description, filename, author_id, url) VALUES (?,?,?,?,?)",(product_title,product_description,filename,g.user['id'], url))
            db.commit()

            return redirect(url_for('product_page.new_product_page', slug=url))

    return render_template('page/add_product_page.html')

def get_product_page(slug):
    product_page = get_db().execute('SELECT title, description, filename FROM product WHERE url=?',(slug,)).fetchone()

    if product_page is None:
        abort(404, "URL {0} doesn't exist. [products]".format(slug))

    return product_page

@bp.route('/product-page/<slug>',methods=('GET','POST'))
def new_product_page(slug):
    product_page = get_product_page(slug)
    return render_template('page/product-page.html', product_page=product_page)

""" """""""""""""""""""OTHER FUNCTIONS"""""""""""""""""""""" """
# Determines if there is a valid file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
