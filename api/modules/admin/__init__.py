r"""The blueprint that handles all the admin-related stuff.
This includes managing students, teachers, admin dashboard, etc.
"""
from flask import Blueprint

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin",
)
