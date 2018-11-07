from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required
from slugify import slugify # generates URL slug
from werkzeug.utils import secure_filename
from flask import current_app as app
import os

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

bp = Blueprint('page', __name__)

@bp.route('/add-page', methods=('GET','POST'))
def add_page():
    if request.method == 'POST':
        page_type = request.form.get('page-types')

        if page_type == 'landing-page':
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
                db = get_db()
                db.execute("INSERT INTO pages (page_type, heading, subheading, button_text, author_id, url) VALUES (?,?,?,?,?,?)",('Landing', heading,subheading,button_text,g.user['id'], url))
                db.commit()

                return redirect(url_for('page.new_page',slug=url))
        elif page_type == 'product-page':
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
                return redirect(url_for('hello'))

    else:
        return render_template('page/add_page.html')

# Determines if there is a valid file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_page(slug):
    page = get_db().execute('SELECT heading, subheading, button_text FROM pages WHERE url=?',(slug,)).fetchone()

    if page is None:
        abort(404, "Page id {0} doesn't exist.".format(id))

    return page

@bp.route('/<slug>',methods=('GET','POST'))
def new_page(slug):
    page = get_page(slug)
    return render_template('page/landing-page.html', page=page)
