r"""The blueprint that handles all the student-related things.
This includes student dashboard, viewing assignments, submitting assignments, etc.
"""
from flask import Blueprint

student = Blueprint(
    "student",
    __name__,
    url_prefix="/api/student",
)
