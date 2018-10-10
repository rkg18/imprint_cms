from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from imprint.db import get_db

from imprint.auth import login_required

@bp.route('/blog')
def blog_index():
    db = get_db()
    posts = db.execute(
        'SELECT p.post_id, title, url, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

""" Add Post function lets user add a blog post to their website """
@bp.route('/add-post', methods=('GET','POST'))
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        body = request.form['body']

    error = None

    if not title:
        error = "A Title is required"
    elif not url:
        error = "A URL is required"

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'INSERT INTO post(title, url, body)'
            ' VALUES (?, ?, ?)',
            (title, url, body)
        )
        db.commit()
        # TODO: Create blog reel in menu
        return redirect()