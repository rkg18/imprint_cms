from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required

bp = Blueprint('blog', __name__)

@bp.route('/blog')
def blog_index():
    db = get_db()
    posts = db.execute(
        'SELECT title, url, body, created'
        ' FROM posts'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/blog.html', posts=posts)

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
            db.execute("INSERT INTO posts (title, body, url) VALUES (?,?,?)",(title,body,url))
            db.commit()

            return redirect(url_for('blog.blog_index'))

    return render_template('blog/add_post.html')
