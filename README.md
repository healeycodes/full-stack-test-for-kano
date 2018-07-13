## Full Stack Development Test

![alt text](https://github.com/healeycodes/full-stack-test-for-kano/blob/master/preview.png "Preview image of app")

A Flask blog application, serving one mobile-first responsive page that accepts user messages via an HTML form. Messages are saved to an SQLite database within the package folder and can be retrieved with an included Python script.

### Build

`pip install -r requirements.txt` or alternatively you can just `pip install Flask`

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

Print all messages, delimited by pipe symbol

`python print_messages.py`

(Optional) add the hardcoded test message

`python print_messages.py add_test_msg`
