import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TOKEN = os.environ.get('TOKEN') or '1286782199:AAEgozwDkYV1s4Fmjd2A_eWLv5BZsHj-Ev8'
    HOST_URL = os.environ.get('HOST_URL') or 'https://f7c65272f9c4.ngrok.io'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['playersoft1999@gmail.com']
