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
def get_grades():
    """Gets grades of assignments parent's students

    Returns
    -------
    dict
        The view response
    """
    students = []
    for student_id in parent.children:
        students.append(Student.get_by_id(student_id))

    grades = []
    for student in students:
        student_assignments = student.get_assignments()
        grades_student = []
        for assignment in student_assignments:
            grade_data = {
            'assignment': assignment.title,
            'grade': assignment.submissions[-1].grade
            }
            grades_student.append(grade_data)

        grade_data = {
            'student': student.first_name + ' ' + student.last_name
            'grades': grades_student
        }
        grades.append(grade_data)

    return response(data={"grades": grades})
