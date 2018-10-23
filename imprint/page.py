from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required

bp = Blueprint('Page', __name__)

@bp.route('/landing-page', methods=('GET','POST'))
def landing_page():
    if request.method == 'POST':
        pass

@bp.route('/product-page')
def product_page():
    pass
