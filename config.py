import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'kjrkf23jrdc3kj'
    FLASK_APP = 'app.py'
    TEMPLATES_FOLDER = 'templates'
