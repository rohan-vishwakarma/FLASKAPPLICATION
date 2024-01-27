import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    SECRET_KEY = "b'x/~\xe2\xdd\n\xe4\x12\x03R\xc2\xe6'"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Friend14@localhost/flask'
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True


    CELERY = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost'
    # CELERY_TASK_IGNORE_RESULT = True
    # CELERY_REDIS_PORT = 6380