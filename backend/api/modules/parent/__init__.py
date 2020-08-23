r"""The blueprint that handles all the parent-related things.
This includes parent dashboard, communication with teachers, and more.
"""
from flask import Blueprint

parent = Blueprint(
    "parent",
    __name__,
    url_prefix="/api/parent",
)

from . import routes
