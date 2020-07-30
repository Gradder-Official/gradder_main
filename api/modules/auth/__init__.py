r"""The blueprint that handles all the authentication.
This includes logging in/out, password reset/changes, etc.
"""
from flask import Blueprint

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)

from . import routes