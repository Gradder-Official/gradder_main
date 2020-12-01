r"""The blueprint that handles all the parent-related things.
This includes parent dashboard, communication with teachers, and more.
"""
from flask import Blueprint

from . import routes

parent = Blueprint(
    "parent",
    __name__,
    url_prefix="/api/parent",
)
