from flask import Blueprint

student = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')