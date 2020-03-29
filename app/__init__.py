from flask import Flask
from flask_login import LoginManager
import firebase_admin
from config import config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    firebase_admin.initialize_app()

    from . import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .modules.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .modules.error_handler import error_handler as error_handler_blueprint
    app.register_blueprint(error_handler_blueprint)

    return app