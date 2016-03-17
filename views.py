import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request, session, url_for

app = Flask(__name__)
app.config.from_object('_config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

# helper functions

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You shall not pass!')
            return redirect(url_for('login'))
    return wrap

def logout():
    session.pop('logged_in', None)
    flash('Peace bitches!')
    return redirect(url_for('login'))


# routes

@app.route('/', methods=['GET', 'POST'])
def themainpage():
    return render_template('themainpage.html')
