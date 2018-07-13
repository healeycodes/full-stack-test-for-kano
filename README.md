## Full Stack Development Test

A Flask blog application, serving one mobile-first responsive page that accepts user messages via an HTML form. Messages are saved to an sqlite database within the package folder and can be retrieved with an included Python script.

### Build

`cd kano_blog`
`python create_db.py`

### Run for development

Flask local server with debugging on:
```
python create_db.py
python app.py

 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 111-709-776
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Run for production

`pip install waitress`

```
python create_db.py
waitress-serve --call 'kano_blog:create_app'

Serving on http://0.0.0.0:8080
```

Docs: http://flask.pocoo.org/docs/1.0/tutorial/deploy/?highlight=deploy


### Get user messages

Add test message
`print_messages.py add_test_msg`

Print all messages, delimited by pipe symbol
`python print_messages.py`
