import os.path
import sys
import sqlite3
from pathlib import Path

DATABASE = 'db.sqlite'
SCHEMA = 'schema.sql'
db_path = str(Path(sys.path[0]) / DATABASE)
schema_path = str(Path(sys.path[0]) / SCHEMA)


def create_db():
    # test if schema exists
    if os.path.isfile(schema_path):

        # connect to, or create database
        db = sqlite3.connect(db_path)
        with open(schema_path) as f:

            # execute schema
            db.executescript(f.read())
        print('Database initialized.')
    else:
        print('{0} not found.'.format(schema_path))


# if ran as main, create db
if __name__ == '__main__':
    create_db()
