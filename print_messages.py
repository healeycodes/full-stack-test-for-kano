import sqlite3
import sys

from pathlib import Path

DATABASE = 'db.sqlite'
db_path = str(Path(sys.path[0]) / 'kano_blog' / DATABASE)


# get all messages, delimited by pipe symbol
def get_messages(source='prod'):
    messages = []
    if source == 'prod':
        db = sqlite3.connect(db_path)
    else:
        db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute('''SELECT email, name, message FROM comment''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        messages.append('{0} | {1} | {2}'.format(row[0], row[1], row[2]))
    db.close()
    return messages


# adds a test message to an already initialized comment table
def add_test_message():
    db_file = Path(db_path)
    if db_file.is_file():
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
    cursor.execute('''INSERT INTO comment (email, name, message)
                  VALUES(?,?,?)''', ('alice@kano.me', 'alice', 'Test msg.'))
    db.commit()
    db.close()


# if ran as main, print all messages
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'add_test_msg':
        add_test_message()
        print('Added test message.')
    else:
        if len(get_messages()) == 0:
            print('No messages in table.')
        else:
            for msg in get_messages():
                print(msg)
