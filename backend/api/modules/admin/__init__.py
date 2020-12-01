r"""The blueprint that handles all the admin-related stuff.
This includes managing students, teachers, admin dashboard, etc.
"""
from flask import Blueprint

from . import routes

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin",
)
