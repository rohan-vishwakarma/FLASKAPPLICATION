import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Friend14@localhost/flask'

    SQLALCHEMY_TRACK_MODIFICATIONS = False