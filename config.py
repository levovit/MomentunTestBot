import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TOKEN = os.environ.get('TOKEN') or ''
    HOST_URL = os.environ.get('HOST_URL') or 'https://cd6e48a714f0.ngrok.io'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['playersoft1999@gmail.com']
