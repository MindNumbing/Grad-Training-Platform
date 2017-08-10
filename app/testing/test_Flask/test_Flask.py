from flask import Flask
from flask_testing import LiveServerTestCase
import urllib2
import unittest


class TestViews(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        return app

    def teardown(self):
        pass

    # Each test below will check ever url possible and if the response code is 200 then the test passes
    def test_connection(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_index(self):
        response = urllib2.urlopen(self.get_server_url()+"/index")
        self.assertEqual(response.code, 200)

    def test_new_orders(self):
        response = urllib2.urlopen(self.get_server_url() + "/new_order")
        self.assertEqual(response.code, 200)

    def test_orders(self):
        response = urllib2.urlopen(self.get_server_url() + "/orders")
        self.assertEqual(response.code, 200)

    def test_access(self):
        response = urllib2.urlopen(self.get_server_url() + "/access")
        self.assertEqual(response.code, 200)
    # Url tests end here ^^

if __name__ == '__main__':
    unittest.main()

