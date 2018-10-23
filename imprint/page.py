from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required

bp = Blueprint('Page', __name__)

@bp.route('/landing-page', methods=('GET','POST'))
def landing_page():
    if request.method == 'POST':
        page_type = request.form.get('page-types')

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
            # db = get_db()
            # db.execute("INSERT INTO posts (title, body, url) VALUES (?,?,?)",(title,body,url))
            # db.commit()

            # return redirect(url_for('blog.blog_index'))

@bp.route('/product-page')
def product_page():
    pass
