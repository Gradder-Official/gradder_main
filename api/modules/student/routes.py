import uuid
from datetime import datetime

from bson import ObjectId
from flask import abort, current_app, request
from flask_login import current_user

from api import db
from api import root_logger as logger
from api.classes import Student, Submission, User, Course, Assignment
from api.tools.decorators import required_access
from api.tools.factory import error, response
from api.tools.google_storage import download_blob, get_signed_url, upload_blob
from api.tools.search import get, get_all
from . import student
from flask import Flask, jsonify


@student.before_request
@required_access(Student)
def student_verification():
    # Required_access decorator already handled it
    pass

@student.route("/submit/<string:course_id>/<string:assignment_id>", methods=["POST"])
def submit(course_id: str, assignment_id: str):
    """Submit work for an assignment
    Parameters
    ----------
    course_id : str
        The ID of the class for which the assignment was set
    assignment_id : str
        The ID of the assignment
    Returns
    -------
    dict
        The view response
    """
    
    assignment = db.courses.find_one(
        {"assignments._id": ObjectId(assignment_id)},
        {"_id": 0, "assignments": {"$elemMatch": {"_id": ObjectId(assignment_id)}}},
    )["assignments"][0]

    if assignment is not None and course_id in current_user.courses:
        try:
            file_list = []
            files = request.files.getlist('files')
            if files[0].filename:
                for file_ in files:
                    filename = file_.filename
                    blob = upload_blob(
                        uuid.uuid4().hex + "." + file_.content_type.split("/")[-1], file_
                    )
                    file_list.append((blob.name, filename))
            
            submission = Submission(
                date_submitted=datetime.utcnow(),
                content=request.form['content'],
                filenames=file_list,
                student_id=current_user.id,
                assignment_id=assignment_id
            )
            
            current_user.add_submission(
                current_user.id, course_id, submission=submission
            )
        except KeyError:
            return error("Not all fields satisfied"), 400
        else:
            logger.info(f"Submission {submission.id} made")
            return response(["Submission was a success"]), 200
    else:
        return error("No assignment found"), 404

@student.route("/assignments", methods=["GET"])
def assignments():
    """Get all assignments for the signed in user
    Returns
    -------
    dict
        The view response
    """
    logger.info(f"Accessed all assignments")
    return response(data={'assignments': current_user.get_assignments()})

@student.route("/assignments/<string:course_id>/", methods=["GET"])
def assignments_by_class(course_id: str):
    """Get assignments for a specific class
    Parameters
    ----------
    course_id : str
        The ID of the class
    Returns
    -------
    dict
        The view response
    """

    course_assignments = Course.get_by_id(course_id).get_assignments()
    logger.info(f"All assignments from {course_id}.")
    return response(data={"assignments": course_assignments})
    #return response(data={"assignments": list(map(lambda a: a.to_json(), course_assignments))})

@student.route("/assignments/<string:assignment_id>/", methods=["GET"])
def assignment_by_id(course_id: str, assignment_id: str):
    """Get an assignment by its ID
    Parameters
    ----------
    course_id : str
        The ID of the class
    assignment_id : str
        The ID of the assignment
    Returns
    -------
    dict
        The view response
    """
    assignments = current_user.get_assignments()
    assignment = get(assignments, id=assignment_id)
    logger.info(f"All assignments from {course_id} with assignment id {assignment_id}.")
    return response(data={"assignment": assignment})


@student.route("/assignments/<string:assignment_id>/submissions")
def submissions_by_assignment_id(assignment_id: str):
    assignments = current_user.get_assignments()
    assignment = get(assignments, id=assignment_id)
    submissions = get_all(assignment.submissions, student_id=current_user.id)

    return response(data={"submissions": submissions})
    

@student.route("/assignment-schedule", methods=["GET"])
def get_schedule_assignments():
    """Gets name and dates for assignments

    Returns
    -------
    dict
        The view response
    """

    assignments = current_user.get_assignments()
    events = []
    for assignment in assignments:
        assignment_data = {
            'title': assignment.title,
            'date': assignment.due_by
        }
        events.append(assignment_data)

    # Dummy event for testing
    dummy_data = [{
        "title": "Test assignment",
        "date": "2020-08-09",
    }]
    events.append(dummy_data)

    return response(data={"events": events})

@student.route("/class-schedule", methods=["GET"])
def get_schedule_classes():
    """Gets name, dates, and times for classes

    Returns
    -------
    dict
        The view response
    """
    
    student_course_ids = current_user.get_course_ids()
    class_schedule = list()
    for student_course in student_course_ids:
        data = Course.get_by_id(student_course)
        course_data = {
            'name': data.name,
            'daysOfWeek': data.schedule_days,
            'startTime': data.schedule_time
        }
        class_schedule.append(course_data)
        
    return response(data={"class_schedule": class_schedule})


@student.route("/activate_account/<string:token>", methods=["POST"])
def activate_account(token: str):
    """Activates the account (while not authenticated)

    Parameters
    ----------
    token : str
        The activation token

    Returns
    -------
    dict
        The view response
    """
    student = Student.verify_activation_token(token)
    if student is None:
        return error("That is an expired or incorrect link."), 400
    else:
        db.students.update({"id": ObjectId(student._id)}, {"$set": {"activated": True}})
        return response(["Account activated!"]), 200

@student.route("/enter_info", methods=["POST"])
def enter_info():
    """Enters description, date of birth and profile picture for student

    Returns 
    -------
    dict
        Flashes, student data from the form
    """

    flashes = list()
    user = Student.get_by_id(current_user.id)

    if request.form.get('description'):
        user.description = request.form["description"]
        flashes.append("Description updated")

    if request.form.get('date_of_birth'):
        user.date_of_birth = request.form["date_of_birth"]
        flashes.append("Date of birth updated")

    try:       
        profile_picture_file = request.files['profile_picture']
        filename = profile_picture_file.filename
        blob = upload_blob(
            uuid.uuid4().hex + "." +  profile_picture_file.content_type.split("/")[-1],
             profile_picture_file,
        )
        profile_picture = (blob.name, filename)

    except KeyError:
            return error("Not all fields satisfied"), 400    

    user.profile_picture = profile_picture
    flashes.append("Profile picture updated")

    logger.info(f"User info {user.id} updated")
    return response(flashes), 200
