from flask import (Flask, g, render_template, flash, redirect, url_for, abort)

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
@app.route('/entries')
def index():
    return render_template('index.html')


@app.route('/entries/new', methods=('GET', 'POST'))
def new_entry():
    new_entry = forms.PostForm()
    if new_entry.validate_on_submit():
        models.Post.create(
            title=new_entry.title.data.strip(),
            date=new_entry.data.strip(),
            time_spent=new_entry.time_spent.data.strip(),
            content=new_entry.content.data.strip(),
            resources=new_entry.resources.data.strip()
        )
        flash("New Entry Made! Thanks!", "success")
        return redirect(url_for('index'))
    return render_template('new.html', new_entry=new_entry)


@app.route('/entries/<int:entry_id>')
def view_entry(entry_id):
    entries = models.Post.select().where(models.Post.id == entry_id)
    return render_template('detail.html', entries=entries)


@app.route('/entries/<id>/edit')
def edit_entry():
    return render_template('edit.html')


#@app.route('/entries/<id>/delete')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host= HOST, port=PORT)
