from dotenv import load_dotenv, find_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv(find_dotenv())
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '329v8qrvnkjehgioqrgh3$##$#UOJ`3r0'
    MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    GRADDER_EMAIL = 'team@gradder.io'
    MAIL_SUBJECT_PREFIX = '[Gradder]'
    MAIL_SENDER = 'Gradder Team <team@gradder.io>'

    SSL_REDIRECT = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        SSL_REDIRECT = True
        Config.init_app(app)

        # Add the logging on production later


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}
