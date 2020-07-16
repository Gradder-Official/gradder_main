from flask import Blueprint

student = Blueprint(
    "student",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/student",
)

from . import routes, forms
