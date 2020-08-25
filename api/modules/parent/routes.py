import uuid
from datetime import datetime

from bson import ObjectId
from flask import abort, current_app, request
from flask_login import current_user

from api import db
from api import root_logger as logger
from api.classes import Parent, Submission, User, Course, Assignment
from api.tools.decorators import required_access
from api.tools.factory import error, response
from api.tools.google_storage import download_blob, get_signed_url, upload_blob
from api.tools.search import get, get_all
from . import parent
from flask import Flask, jsonify


@parent.before_request
@required_access(Parent)
def parent_verification():
    # Required_access decorator already handled it
    pass

@parent.route("/check-grades/<string:course_id>/", methods=["GET"])
def get_schedule_classes(course_id: str):
    """Gets grades of assignments for specific course of a student

    Returns
    -------
    dict
        The view response
    """
        
    course_assignments = Course.get_by_id(course_id).get_assignments()
    grades = []
    for assignment in course_assignments:
        grade_data = {
            'assignment': assignment.title,
            'grade': assignment.submissions[-1].grade
        }
        grades.append(grade_data)
    
    return response(data={"grades": grades})
