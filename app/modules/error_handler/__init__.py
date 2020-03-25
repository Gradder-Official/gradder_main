from flask import Blueprint

error_handler = Blueprint('error_handler', __name__)

from . import routes