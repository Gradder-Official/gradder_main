from flask import Blueprint

admin = Blueprint(
    "admin",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/admin",
)

from . import routes, forms
