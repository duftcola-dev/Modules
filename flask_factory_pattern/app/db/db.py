import sqlite3
from flask import current_app,g 
from flask.cli import with_appcontext

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE_URI"],
            detect_types=sqlite3.PARSE_DECLTYPES
            )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db",None)
    if db is not None:
        db.close()
    

def init__app(app):
    app.teardown_appcontext(close_db)


