""" Blueprint for Authorizing (Login and Register) a User """
import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from imprint.db import get_db # calls functions for database

""" Creates instance of blueprint object """
bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register', method=('GET','POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        db = get_db() # Calls from DB module

        error = None # placeholder variable for error messages

        # Validates user input
        if not email:
            error = 'Email is required'
        elif not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone() is not None:
            error = 'User {} is alraedy registered'.format(username)

        # if all info is valid then add to database table 'user'
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
