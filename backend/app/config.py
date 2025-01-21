import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'admin')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '9900')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5432)
    DB = os.environ.get('POSTGRES_DB', 'movies')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False