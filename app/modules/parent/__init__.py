from flask import Blueprint

student = Blueprint('parent', __name__, static_folder='static', template_folder='templates', url_prefix='/parent')