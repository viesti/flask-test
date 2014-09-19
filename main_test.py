import requests
from flask import Flask
from flask.ext.testing import LiveServerTestCase
import main

class MyTest(LiveServerTestCase):

    def create_app(self):
        main.app.config['TESTING'] = True
        # Default port is 5000
        main.app.config['LIVESERVER_PORT'] = 8943
        return main.app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)

    def test_greeting(self):
        response = requests.get(self.get_server_url() + "/greet/tester?foo=bar")
        self.assertEqual(response.text, "Hello: tester")
        print "args: %s" % main.args
