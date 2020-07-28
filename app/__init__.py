from flask import Flask
from flask_login import LoginManager

from app.db import DB
from app.mixins import JSONImproved
from config import config
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_talisman import Talisman

login_manager = LoginManager()
login_manager.login_view = "auth.login"

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()

db = DB("school1")


def create_app(config_name):
    app = Flask(__name__)
    # Set default encoder to improved one which handles ObjectIds and
    # converts them to strings
    app.json_encoder = JSONImproved

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    if app.config["SSL_REDIRECT"]:
        from flask_sslify import SSLify

        sslify = SSLify(app)

    with app.app_context():
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        from .modules.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        from .modules.student import student as student_blueprint
        app.register_blueprint(student_blueprint)

        from .modules.parent import parent as parent_blueprint
        app.register_blueprint(parent_blueprint)

        from .modules.admin import admin as admin_blueprint
        app.register_blueprint(admin_blueprint)

        from .modules.teacher import teacher as teacher_blueprint
        app.register_blueprint(teacher_blueprint)

        return app
