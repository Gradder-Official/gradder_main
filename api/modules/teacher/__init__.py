"""The blueprint that handles teacher routes
"""
from flask import Blueprint

teacher = Blueprint(
    "teacher",
    __name__,
    url_prefix="/teacher",
)
