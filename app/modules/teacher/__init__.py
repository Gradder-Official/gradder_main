from flask import Blueprint

teacher = Blueprint('teacher', __name__, static_folder='static', template_folder='template', url_prefix='/teacher')