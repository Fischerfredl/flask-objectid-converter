import unittest
import bson

import flask

import flask_objectid_converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        app = flask.Flask(__name__)

        app.url_map.converters['objectid'] = flask_objectid_converter.ObjectIDConverter

        @app.route('/')
        def index():
            return 'Index'

        @app.route('/<objectid:oid>')
        def convert(oid):
            return str(oid)

        app.config['SERVER_NAME'] = 'localhost'

        self.app = app
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_convert(self):
        oid = bson.ObjectId('12345678900987654321aabb')

        with self.app.test_request_context('/'):
            url = flask.url_for('convert', oid=oid)
            self.assertIsInstance(url, str)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('12345678900987654321aabb', response.data.decode())

    def test_404(self):
        response = self.client.get('/notvalid')

        self.assertEqual(response.status_code, 404)
