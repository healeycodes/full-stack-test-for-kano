import sqlite3
import sys

from pathlib import Path

from flask import g, Flask, flash, render_template, request

# create Flask instance
app = Flask(__name__)
app.secret_key = 'secret'
app.config['DATABASE'] = 'db.sqlite'

# sqlite database will stored be in package dir for MVP
db_path = str(Path(app.root_path) / app.config['DATABASE'])


# get an sqlite connection to db
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path)
    return db


# when the current request finishes, close any db connections
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# the only route for our MVP - a blog post
@app.route('/', methods=('GET', 'POST'))
def post():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        message = request.form['message']

        get_db().execute(
            'INSERT INTO comment (email, name, message) VALUES (?, ?, ?)',
            (email, name, message)
        )
        get_db().commit()

        flash('Thank you!')

    return render_template('post.html')


# if ran as main, run Flask development server
if __name__ == '__main__':
    app.run(debug=True)
