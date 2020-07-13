from app.db import DB
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_talisman import Talisman
from config import config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()

db = DB('school1')


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)


    # if config[config_name].SSL_REDIRECT:
    #     Talisman(app)

    # cred = credentials.Certificate(app.config["FIREBASE_CERTIFICATE"])
    # firebase_admin.initialize_app(cred)

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
