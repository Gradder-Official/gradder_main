"""The blueprint that handles parent routes
"""
from flask import Blueprint

parent = Blueprint(
    "parent",
    __name__,
    url_prefix="/parent",
)
