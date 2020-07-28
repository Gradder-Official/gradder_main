from flask_login import LoginManager

from api.tools.db import DB
from config import config
from flask_mail import Mail
from .tools.encoder import JSONImproved


login_manager = LoginManager()
login_manager.login_view = "auth.login"

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.json_encoder = JSONImproved

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # TODO: Add handling of different schools based on the information passed from the React frontend
    db = DB("school1")  

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