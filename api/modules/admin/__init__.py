"""The blueprint that handles admin routes
"""
from flask import Blueprint

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)

from . import routes