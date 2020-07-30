from typing import Union

from flask import abort, current_app, redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from api import db, login_manager
from api import root_logger as logger
from api.classes import Admin, Parent, Student, Teacher, User
from api.tools.dictionaries import TYPE_DICTIONARY
from api.tools.factory import error, response
from api.tools.decorators import required_access

from . import student


@student.before_request
@required_access(Student)
def student_verification():
    # Required_access decorator already handled it
    pass


@student.route("/submit/<string:class_id>/<string:assignment_id>", methods=["POST"])
def submit(class_id: str, assignment_id: str):
    """Submit work for an assignment

    Parameters
    ----------
    class_id : str
        The ID of the class for which the assignment was set
    assignment_id : str
        The ID of the assignment

    Returns
    -------
    dict
        The view response
    """
    pass


@student.route("/assignments", methods=["GET"])
def assignments():
    """Get all assignments for the signed in user

    Returns
    -------
    dict
        The view response
    """
    pass


@student.route("/assignments/<string:class_id>/", methods=["GET"])
def assignments_by_class(class_id: str):
    """Get assignments for a specific class

    Parameters
    ----------
    class_id : str
        The ID of the class

    Returns
    -------
    dict
        The view response
    """
    pass


# This could possibly instead just use /assignments/<string:assignment_id>/
# and then we could search through classes to find the assignment 
@student.route("/assignments/<string:class_id>/<string:assignment_id>/", methods=["GET"])
def assignment_by_id(class_id: str, assignment_id: str):
    """Get an assignment by its ID

    Parameters
    ----------
    class_id : str
        The ID of the class
    assignment_id : str
        The ID of the assignment

    Returns
    -------
    dict
        The view response
    """
    pass