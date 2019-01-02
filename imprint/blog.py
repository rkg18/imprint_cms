from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from imprint.db import get_db
from imprint.auth import login_required
from slugify import slugify # generates URL slug

bp = Blueprint('blog', __name__)

@bp.route('/blog')
def blog_index():
    db = get_db()
    posts = db.execute(
        'SELECT post_id, title, url, body, created, author_id, username'
        ' FROM posts p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/blog.html', posts=posts)

""" Add Post function lets user add a blog post to their website """
@bp.route('/add-post', methods=('GET','POST'))
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        url = slugify(title)
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
            db.execute("INSERT INTO posts (title, body, url, author_id) VALUES (?,?,?,?)",(title,body,url,g.user['id']))
            db.commit()

            return redirect(url_for('blog.blog_index'))

    return render_template('blog/add_post.html')

""" Individual Post Page """
def get_post(id):
    post = get_db().execute('SELECT post_id, title, body, created, url, author_id, username FROM posts p JOIN user u on p.author_id = u.id WHERE post_id=?',(id,)).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return post

""" Edit feature """
@bp.route('/blog/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_post(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE posts SET title = ?, body = ? WHERE post_id = ?',(title,body,id))
            db.commit()
            return redirect(url_for('blog.blog_index'))

    return render_template('blog/edit_post.html', post=post)

@bp.route('/blog/<int:id>/delete', methods=('POST',))
@login_required
def delete_post(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM posts WHERE post_id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.blog_index'))

@bp.route('/blog/<int:id>/<slug>',methods=('GET','POST'))
@login_required
def post(id, slug):
    post = get_post(id)
    return render_template('blog/post.html', post = post)
