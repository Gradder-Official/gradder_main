from flask import Blueprint

parent = Blueprint('parent', __name__, static_folder='static', template_folder='templates', url_prefix='/parent')

from . import routes, forms
