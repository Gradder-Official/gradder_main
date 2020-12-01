from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS

from config import config

from .tools.encoder import JSONImproved
from .tools.db import DB
from .classes import SchoolConfig
from .tools.logger import logger


login_manager = LoginManager()
login_manager.login_view = "auth.login"

mail = Mail()

db: DB = None
school_config: SchoolConfig = None
root_logger: logger = None


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.json_encoder = JSONImproved

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # TODO: Add handling of different schools based on the information passed from the React frontend
    global db
    db = DB(app.config.get("MONGO_CONNECTION_STRING"), "school1")

    global school_config
    school_config = SchoolConfig()

    global root_logger
    # Creates a logger relevant to the app environment
    root_logger = logger[config_name]()

    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
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
