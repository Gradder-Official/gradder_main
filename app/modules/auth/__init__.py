from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='folder', static_folder='static')

from . import routes