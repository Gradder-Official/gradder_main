r"""The blueprint that handles all the authentication.
This includes logging in/out, password reset/changes, etc.
"""
from . import routes
from flask import Blueprint

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth",
)
