import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""
            CREATE TABLE rsvps
            (rsvp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL)""")

    c.execute(
            'INSERT INTO rsvps (name, email)'
            'VALUES("Hamlet Booger", "hamlet.booger@gmail.com")'
    )

    c.execute(
            'INSERT INTO rsvps (name, email)'
            'VALUES("Howard Moon", "howard.moon@gmail.com")'
    )
