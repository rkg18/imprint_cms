from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from imprint.db import get_db

bp = Blueprint('dashboard',__name__, url_prefix='/dashboard')

@bp.route('/admin')
def admin():
    return render_template('dashboard/admin.html')
