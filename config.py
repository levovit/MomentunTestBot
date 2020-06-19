import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TOKEN = os.environ.get('TOKEN')
    HOST_URL = os.environ.get('HOST_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['playersoft1999@gmail.com']
