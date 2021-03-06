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

@bp.route('/product-page')
def product_index():
    pages = get_db().execute('SELECT title, url, author_id FROM product').fetchall()

    return render_template('product_page/product_page_index.html', pages=pages)

""" """"""""""""""""""ADDING Product PAGE"""""""""""""""""" """

@bp.route('/add-product-page', methods=('GET','POST'))
def add_product_page():
    db=get_db()

    if request.method == "POST":
        product_title = request.form['product-title']
        product_description = request.form['product-description']
        bulletpoint1 = request.form.get('bulletpoint1')
        bulletpoint2 = request.form.get('bulletpoint2')
        bulletpoint3 = request.form.get('bulletpoint3')
        bulletpoint4 = request.form.get('bulletpoint4')
        bulletpoint5 = request.form.get('bulletpoint5')
        page_layout = request.form['options']
        buy_button_text = request.form['buy-button-text']
        buy_button_link = request.form['buy-button-link']

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
            db.execute("INSERT INTO product (title, description, filename, author_id, url, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text, buy_button_link) VALUES (?,?,?,?,?,?,?,?,?,?,?,?, ?)",(product_title,product_description,filename,g.user['id'], url, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text, buy_button_link))
            db.commit()

            return redirect(url_for('product_page.new_product_page', slug=url))

    return render_template('product_page/add_product_page.html')

""" Edit feature """
@bp.route('/product-page/<slug>/edit', methods=('GET', 'POST'))
@login_required
def edit_product_page(slug):
    page = get_product_page(slug)

    oldTitle = page['title']

    db = get_db()

    if request.method == 'POST':
        product_title = request.form['product-title']
        product_description = request.form['product-description']
        oldFilename = page['filename']
        bulletpoint1 = request.form.get('bulletpoint1')
        bulletpoint2 = request.form.get('bulletpoint2')
        bulletpoint3 = request.form.get('bulletpoint3')
        bulletpoint4 = request.form.get('bulletpoint4')
        bulletpoint5 = request.form.get('bulletpoint5')
        page_layout = request.form['options']
        buy_button_text = request.form['buy-button-text']
        buy_button_link = request.form['buy-button-link']

        newUrl = slugify(product_title)

        if not product_title:
            error = 'A heading is required'

        # New File Submission
        if 'new_file' not in request.files:
            if(oldTitle != product_title):
                db.execute("INSERT INTO product (title, description, filename, author_id, url, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text,buy_button_link VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?)",(product_title,product_description,oldFilename,g.user['id'], newUrl, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text,buy_button_link))
                db.execute("DELETE FROM product WHERE url=?",(slug,))
            else:
                db.execute("UPDATE product SET description = ?, bulletpoint1 = ?, bulletpoint2 = ?, bulletpoint3 = ?, bulletpoint4 = ?, bulletpoint5 = ?, filename=?, page_layout=?, buy_button_text=?,buy_button_link=? WHERE url = ?",(product_description, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, oldFilename, page_layout, buy_button_text,buy_button_link, newUrl))
            db.commit()
            return redirect(url_for('product_page.new_product_page',slug=newUrl))   
        else:
            new_file = request.files['new_file']
            if new_file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if new_file and allowed_file(new_file.filename):
                filename = secure_filename(new_file.filename)
                new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                if(oldTitle != product_title):
                    db.execute("INSERT INTO product (title, description, filename, author_id, url, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text,buy_button_link) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(product_title,product_description,filename,g.user['id'], newUrl, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text,buy_button_link))
                    db.execute("DELETE FROM product WHERE url=?",(slug,))
                else:
                    db.execute("UPDATE product SET description = ?, bulletpoint1 = ?, bulletpoint2 = ?, bulletpoint3 = ?, bulletpoint4 = ?, bulletpoint5 = ?, filename=?, page_layout=?, buy_button_text=?,buy_button_link=? WHERE url = ?",(product_description, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, filename, page_layout, buy_button_text,buy_button_link, newUrl))
                db.commit()
                return redirect(url_for('product_page.new_product_page',slug=newUrl))   

    return render_template('product_page/edit_product_page.html', product_page=page)

def get_product_page(slug):
    product_page = get_db().execute('SELECT title, description, filename, author_id, url, bulletpoint1,bulletpoint2,bulletpoint3,bulletpoint4,bulletpoint5, page_layout, buy_button_text,buy_button_link FROM product WHERE url=?',(slug,)).fetchone()

    if product_page is None:
        abort(404, "URL {0} doesn't exist. [products]".format(slug))

    return product_page

@bp.route('/product-page/<slug>',methods=('GET','POST'))
def new_product_page(slug):
    product_page = get_product_page(slug)
    if(product_page['page_layout'] == 'imageLeft'):
        return render_template('product_page/product_page_imageLeft.html', product_page=product_page)
    else:
        return render_template('product_page/product_page_imageRight.html', product_page=product_page)

# DELETES Landing Page
@bp.route('/product-page/<slug>/delete', methods=('POST',))
@login_required
def delete_page(slug):
    get_product_page(slug)
    db = get_db()
    db.execute('DELETE FROM product WHERE url = ?', (slug,))
    db.commit()
    return redirect(url_for('product_page.product_index'))

""" """""""""""""""""""OTHER FUNCTIONS"""""""""""""""""""""" """
# Determines if there is a valid file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
