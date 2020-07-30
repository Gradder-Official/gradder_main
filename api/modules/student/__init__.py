"""The blueprint that handles student routes
"""
from flask import Blueprint

student = Blueprint(
    "student",
    __name__,
    url_prefix="/student",
)

from . import routes