import sqlite3, yaml
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

# yamlfiles

AGENDA = yaml.load( open( 'yamlfiles/agenda.yml' ) )
BRIDALPARTY = yaml.load( open( 'yamlfiles/bridalparty.yml' ) )
LODGING = yaml.load( open( 'yamlfiles/lodging.yml' ) )

# routes

@app.route('/', methods=['GET', 'POST'])
def themainpage():
    agenda = AGENDA
    bridalparty = BRIDALPARTY
    lodging = LODGING
    return render_template('themainpage.html', bridalparty=bridalparty, agenda=agenda, lodging=lodging)
