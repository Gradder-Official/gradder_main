import os

from dotenv import find_dotenv
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv(find_dotenv())
    SECRET_KEY = os.environ.get("SECRET_KEY") or "329v8qrvnkjehgioqrgh3$##$#UOJ`3r0"

    MONGO_CONNECTION_STRING = os.environ.get("MONGO_CONNECTION_STRING")

    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() in ["true", "on", "1"]
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    GRADDER_EMAIL = "team@gradder.io"
    MAIL_SUBJECT_PREFIX = "[Gradder]"
    MAIL_SENDER = "Gradder Team <team@gradder.io>"

    SSL_REDIRECT = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class ProductionConfig(Config):
    @classmethod
    def init_app(app):
        SSL_REDIRECT = True
        Config.init_app(app)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": ProductionConfig,
}
