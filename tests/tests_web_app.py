import os
import unittest
from webtest import TestApp
import sys
sys.path.append('../')
from python_webtest import web_app #

os.environ['WEBTEST_TARGET_URL'] = 'http://localhost:8888'
test_app = TestApp(web_app)

class BlackBoxTest(unittest.TestCase):
    """ check when there is query """
    def test_upper_change(self):
        res = test_app.get('/example/foo')
        self.assertEqual(res.status_int, 200)
        self.assertEqual(res.json['upper_query'], 'FOO')

    """ check when there is no query. """
    def test_no_query(self):
        res = test_app.get('/example/')
        self.assertEqual(res.status_int, 200)
        self.assertEqual(res.json['query'], 'NO_QUERY')

class WhiteBoxTest(unittest.TestCase):
    """ check upper case changing. """
    def test_upper_change(self):
        rs = web_app.RootServer()
        self.assertEqual(rs._big_letter("foo"), 'FOO')

if __name__ == '__main__':
    unittest.main()