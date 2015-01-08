# coding: utf-8

from unittest import TestCase
from random import randrange
from findaconf import app
from findaconf.tests.config import set_app, unset_app


class TestFileRoutes(TestCase):

    def setUp(self):
        self.app = set_app(app)

    def tearDown(self):
        unset_app()

    # test routes from blueprint/file_routes.py

    def test_poster(self):
        resp = self.app.get('/poster.png', data={'rand': randrange(100, 999)})
        assert resp.status_code == 200
        assert resp.mimetype == 'image/png'

    def test_favicon(self):
        types = ['image/vnd.microsoft.icon', 'image/x-icon']
        resp = self.app.get('/favicon.ico')
        assert resp.status_code == 200
        assert resp.mimetype in types

    def test_robots(self):
        resp = self.app.get('/robots.txt')
        assert resp.status_code == 200
        assert resp.mimetype == 'text/plain'

    def test_foundation_icons(self):
        base_url = '/assets/'
        extensions = ['eot', 'svg', 'ttf', 'woff', 'py']
        types = ['application/vnd.ms-fontobject',
                 'application/octet-stream',
                 'application/x-font-woff',
                 'image/svg+xml']
        for ext in extensions:
            path = '{}foundation-icons.{}'.format(base_url, ext)
            resp = self.app.get(path)
            if ext != 'py':
                assert resp.status_code == 200
                assert resp.mimetype in types
            else:
                assert resp.status_code == 404
