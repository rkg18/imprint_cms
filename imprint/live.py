from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from imprint.db import get_db
from imprint.auth import login_required

bp = Blueprint('live', __name__)

""" Live Example of the Site """
@bp.route('/<domain>')
@login_required
def live_site(domain):
    user = g.user['username']

    return render_template('live/index.html')

