import uuid
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename

from api import db
from api import root_logger as logger
from api.classes import Assignment, Course, Submission, Teacher
from api.tools.decorators import required_access
from api.tools.factory import error, response
from api.tools.google_storage import upload_blob
from api.tools.search import get

from . import teacher


def get_existing_assignment_files():
    """ Helper function to get existing assignment files
    """
    file_list = []
    files = request.files.getlist(request.form['files'].name)
    if files[0].filename:
        for file_ in files:
            filename = file_.filename
            blob = upload_blob(
                uuid.uuid4().hex + "." + file_.content_type.split("/")[-1], file_
            )
            file_list.append((blob.name, filename))
    
    return file_list

#@teacher.before_request
#@required_access(Teacher)
def teacher_verification():
    # Required_access decorator already handled it
    pass


@teacher.route("/add_assignment", methods=["GET", "POST"])
def add_assignment():
    """Adds new assignment for the class

    Returns
    -------
    dict
        The view response
    """
    request.form['assigned_to'].choices = current_user.get_class_names()

    try:
        file_list = get_existing_assignment_files()

        new_assignment = Assignment(
            date_assigned=datetime.utcnow(),
            assigned_by=current_user.ID,
            assigned_to=request.form['assigned_to'],
            due_by=request.form['due_by'],
            title=request.form['title'],
            content=request.form['content'],
            filenames=file_list,
            estimated_time=request.form['estimated_time'],
            # weight=request.form['weight']
        )

        Course.get_by_id(request.form['assigned_to']).add_assignment(new_assignment)

        logger.info(f"Assignment {request.form['title']} added")
        return response(flashes=["Assignment sent!"])

    except KeyError:
        return error("Not all fields satisfied"), 400


@teacher.route("/courses", methods=["GET"])
def view_assignments():
    """Collects all courses for a specific teatcher.
    Returns
    -------
    dict
        All the courses and their respective data (id, name, and assignments)
    """
    
    courses = []
    for course_id in current_user.courses:
        course = Course.get_by_id(course_id)
        course_assignments = course.get_assignments()
        course_data = {
            'id': str(course_id),
            'name': course.name,
            'assignments': list(map(lambda a: a.to_dict(), course_assignments)),
            'students': course.students,
            'description': course.description,
            'schedule_time': course.schedule_time,
            'schedule_days': course.schedule_days,
            '_syllabus': course._syllabus
        }
        courses.append(course_data)
    
    return response(data={"courses": [course_data]})

@teacher.route("/assignments/<string:course_id>", methods=["GET"])
def view_assignment_by_class_id(course_id: str):
    """Collects assignments from a specific class

    Parameters
    -------
    class_id: str
        The class ID to look up in the database

    Returns
    -------
    dict
        The specified class and its respective data (id, name, and assignments)
    """
    course_assignments = Course.get_by_id(course_id).get_assignments()

    return response(data={"assignments": list(map(lambda a: a.to_dict(), course_assignments))})

@teacher.route("/assignments/<string:course_id>/<string:assignment_id>", methods=["GET", "POST"])
def edit_assignment(course_id: str, assignment_id: str):
    """Edits assignment for the class

    Parameters
    -------
    course_id: str
        The course ID to look up in the database
    
    assignment_id: str
        The assignment ID to look up in the database
    
    Returns
    -------
    dict
        Edited assignment data
    """
    
    course = Course.get_by_id(course_id)
    assignments = course.get_assignments()

    assignment : Assignment = list(filter(lambda a: str(a.id) == assignment_id, assignments))[0]

    if assignment is None:
        return error("Could not find assignment"), 400
    
    try:
        file_list = get_existing_assignment_files()

        edited_assignment = Assignment(
            date_assigned=assignment.date_assigned,
            assigned_by=assignment.assigned_by,
            assigned_to=request.form['assigned_to'],
            due_by=request.form['due_by'],
            title=request.form['title'],
            content=request.form['content'],
            filenames=file_list,
            estimated_time=request.form['estimated_time'],
            # weight=request.form['weight']
        )
        edited_assignment.id = assignment.id
        course.edit_assignment(edited_assignment)
        # Assign to 'assignment' so form has new details
        assignment = edited_assignment

    except KeyError:
        return error("Not all fields satisfied"), 400
    
    # Set default values for form.
    request.form['assigned_to'].default = assignment.assigned_to
    request.form['due_by'].default = assignment.due_by
    request.form['estimated_time'].default = assignment.estimated_time
    request.form['title'].default = assignment.title
    request.form['content'].default = assignment.content
    # request.form['weight'].default = assignment.weight
    request.files.default = assignment.filenames

    return response(data={"assignment":assignment.to_json()})

@teacher.route("/course/<string:course_id>", methods=["GET", "POST"])
def manage_classes_by_id(course_id: str):
    """Updates a specified course's information

    Parameters
    -------
    course_id: str
        The course ID to look up in the database
    
    Returns
    -------
    dict
        Class data (id and name)
        Current class description
    """
    course = Course.get_by_id(course_id)
    syllabus_name = course.get_syllabus_name()

    if syllabus_name is not None:

        if len(syllabus_name) > 20:
            syllabus_name = syllabus_name[:20] + "..."

        request.form['syllabus'].label.text = (
            f"Update current syllabus: { syllabus_name })"
        )

    else:
        return error("Could not find syllabus"), 400

    try:
        syllabus = ()
        if request.form['syllabus'].name is not None:
            syllabus_file = request.files[request.form['syllabus'].name]
            filename = syllabus_file.filename
            blob = upload_blob(
                uuid.uuid4().hex + "." + syllabus_file.content_type.split("/")[-1],
                syllabus_file,
            )
            syllabus = (blob.name, filename)
        else:
            return error("Please specify the syllabus name"), 400
        
        course.update_description(request.form['description'])
        course.update_syllabus(syllabus)

        logger.info(f"Syllabus updated")
        return response(flashes=["Course information successfully updated!"])

    except KeyError:
        return error("Not all fields satisfied"), 400

    courses = []
    for course_id in current_user.courses:
        course_data = {
            'id': str(course_id),
            'name': Course.get_by_id(course_id).name,
        }
        courses.append(course_data)

    return response(
        flashes=["Course information successfully updated!"], 
        data={"courses": courses, "current_description": course.description}
    )

@teacher.route("/activate_account/<string:token>", methods=["POST"])
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
    teacher = Teacher.verify_activation_token(token)
    if teacher is None: 
        return error("That is an expired or incorrect link."), 400
    else:
        db.teachers.update({"id": teacher.id}, {"$set": {"activated": True}})
        return response(["Account activated!"]), 200 

@teacher.route("/course/<string:course_id>/assignments/<string:assignment_id>/submissions", methods=["GET"])
def view_submissions_by_assignment(course_id: str, assignment_id: str):
    """Collects all submissions for a specific assignment of a class

    Parameters
    -------
    course_id: str
        The course ID to look up in the database
    
    assignment_id: str
        The assignment ID to look up in the database

    Returns
    -------
    dict
        Assignment submissions
    """
    course = Course.get_by_id(course_id)
    assignments = course.get_assignments()

    assignment: Assignment = list(filter(lambda a: str(a.id) == assignment_id, assignments))[0]

    if assignment is None:
        return error("Could not find assignment"), 400

    else:
        return response(data={"submissions": assignment.submissions})

@teacher.route("/course/<string:course_id>/assignments/<string:assignment_id>/submissions/<string:submission_id>", methods=["POST"])
def mark_submission(course_id: str, assignment_id: str, submission_id: str):
    flashes = []
    
    course = Course.get_by_id(course_id)
    assignments = course.get_assignments()
    assignment: Assignment = get(assignments, id=assignment_id)
    submission: Submission = get(assignment.submissions, id=submission_id)
    
    min_, max_ = course.grade_range
    if min_ < request.form['grade'] < max_:
        submission.update_grade(request.form['grade'])
        flashes.append("Grade updated!")
        return response(flashes), 200
    
    return error("Grade outside course grade boundary")
 

@teacher.route("/enter_info", methods=["POST"])
def enter_info():
    """Enters description, date of birth and profile picture for teacher

    Returns 
    -------
    dict
        Flashes, teacher data from the form
    """
    
    flashes = list()
    user = Teacher.get_by_id(current_user.id)

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
