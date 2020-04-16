from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
import firebase_admin
from firebase_admin import credentials
from config import config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()

from .modules.db.api import DB
db = DB()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    cred = credentials.Certificate(app.config["FIREBASE_CERTIFICATE"])
    firebase_admin.initialize_app(cred)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .modules.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .modules.error_handler import error_handler as error_handler_blueprint
    app.register_blueprint(error_handler_blueprint)

    return app