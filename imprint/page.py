from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required
from slugify import slugify

bp = Blueprint('page', __name__)

@bp.route('/landing-page', methods=('GET','POST'))
def landing_page():
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
    else:
        return render_template('page/add_page.html')

@bp.route('/<slug>',methods=('GET','POST'))
@login_required
def new_page(slug):
    return render_template('page/page.html')

@bp.route('/product-page')
def product_page():
    pass
