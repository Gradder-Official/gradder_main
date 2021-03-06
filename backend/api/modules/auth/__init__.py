r"""The blueprint that handles all the authentication.
This includes logging in/out, password reset/changes, etc.
"""
from flask import Blueprint

from . import routes

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth",
)
