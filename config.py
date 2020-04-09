import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '329v8qrvnkjehgioqrgh3$##$#UOJ`3r0'
    FIREBASE_CERTIFICATE = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') or \
        "C:\\Users\\vika_\\Desktop\\Projects\\Gradder\\new_app\\credentials\\firebase_key.json"

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
        Config.init_app(app)

        # Add the logging on production later


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}   