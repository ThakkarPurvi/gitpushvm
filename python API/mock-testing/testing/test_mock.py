import requests_mock
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    def test_football(self):
    # We will mock a response of 1 and test that we get football returned.
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number' , text ="1")
            m.get('http://api:5000/get/letter' , text ="a")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)

    def test_badminton(self):
    # We will mock a response of 1 and test that we get badminton returned.
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number' , text ="1")
            m.get('http://api:5000/get/letter' , text ="b")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)

    def test_hockey(self):
    # We will mock a response of 1 and test that we get hockey returned.
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number' , text ="1")
            m.get('http://api:5000/get/letter' , text ="c")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)

    def test_Boxing(self):
    # We will mock a response of 1 and test that we get Boxing returned.
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number' , text ="1")
            m.get('http://api:5000/get/letter' , text ="d")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)