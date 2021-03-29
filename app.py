from flask import (Flask, g, render_template, flash, redirect, url_for, abort, request)

import models
import forms

DEBUG = True
PORT = 8002
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'keryhpioewqyr9kjashdkjh'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries', methods=('GET', 'POST'))
def home():
    stream = models.Post.select().order_by(models.Post.date.desc())
    return render_template('home.html', stream=stream)


@app.route('/entries/new', methods=('GET', 'POST'))
def new_entry():
    journal_entry = forms.PostForm()
    if journal_entry.validate_on_submit():
        models.Post.create(
            title=journal_entry.title.data.strip(),
            date=journal_entry.date.data,
            time_spent=journal_entry.time_spent.data,
            content=journal_entry.content.data.strip(),
            resources=journal_entry.resources.data.strip()
        )
        flash("New Entry Made!", "success")
        return redirect(url_for('home'))
    return render_template('new.html', new_entry=journal_entry)


@app.route('/entries/<int:entry_id>')
def view_entry(entry_id):
    entries = models.Post.select().where(models.Post.id == entry_id)
    return render_template('detail.html', stream=entries)


# referenced https://github.com/andradm/Journal-project/blob/main/app.py for application and understanding of how
# to edit an entry
@app.route('/entries/<int:entry_id>/edit', methods=('GET', 'POST'))
def edit_entry(entry_id):
    entry = models.Post.get(models.Post.id == entry_id)
    form = forms.PostForm()
    if request.method == 'GET':
        form.title.data = entry.title
        form.date.data = entry.date
        form.time_spent.data = entry.time_spent
        form.content.data = entry.content
        form.resources.data = entry.resources
    elif form.validate_on_submit():
        entry.title = form.title.data
        entry.time_spent = form.time_spent.data
        entry.content = form.content.data
        entry.resources = form.resources.data
        entry.date = form.date.data
        entry.save()
        flash("Entry updated!", "success")
        return redirect(url_for('home', entry_id=entry_id))
    return render_template('edit.html', form=form, entry=entry)


@app.route('/entries/<int:entry_id>/delete')
def delete_entry(entry_id):
    entry = models.Post.get(models.Post.id == entry_id)
    entry.delete_instance()
    flash("Entry deleted!", "success")
    return redirect(url_for('home'))


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
