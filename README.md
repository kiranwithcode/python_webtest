# python_webtest
This is my way python example which tests web application in black-box/white-box way with `unittest` & `webtest`.

## Description
- `web_app.py`
    - sample `cherrypy` web application which returns json.
    - if there is the query as sub URL, return upper case of the query.
- `tests/test_web_app.py`
    - test code of `web_app.py`
    - `BlackBoxTest` checks the http status code & the json response.
    - `WhiteBoxTest` checks the internal method's behavior.

## Run & Result

```
$ python -V
Python 3.6.0

# run web app
$ python web_app.py
[04/Jun/2017:16:54:20] ENGINE Listening for SIGTERM.
[04/Jun/2017:16:54:20] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[04/Jun/2017:16:54:20] ENGINE Set handler for console events.
[04/Jun/2017:16:54:20] ENGINE Started monitor thread 'Autoreloader'.
[04/Jun/2017:16:54:20] ENGINE Started monitor thread '_TimeoutMonitor'.
[04/Jun/2017:16:54:20] ENGINE Serving on http://127.0.0.1:8888
[04/Jun/2017:16:54:20] ENGINE Bus STARTED

# check sample application by curl
$ curl localhost:8888/example/foo -s
{"query": "foo", "upper_query": "FOO"}

$ curl localhost:8888/example/ -s
{"query": "NO_QUERY"}

# run tests
$ python -m unittest tests/tests_web_app.py -v
test_no_query (tests.tests_web_app.BlackBoxTest) ... ok
test_upper_change (tests.tests_web_app.BlackBoxTest) ... ok
test_upper_change (tests.tests_web_app.WhiteBoxTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 2.012s

OK

```

