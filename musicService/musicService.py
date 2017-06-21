import os
from tinydb import TinyDB
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
    
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'music.json'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    db = TinyDB(app.config['DATABASE'])
    return db

def get_db():
    if not hasattr(g, 'tinydb'):
        g.tinydb = connect_db()
        
    return g.tinydb

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'tinydb'):
        g.tinydb.close()
    