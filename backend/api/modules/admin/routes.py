import uuid

from flask import current_app, request, url_for
from flask_login import current_user
from flask_mail import Message

from api import mail
from api import root_logger as logger
from api.classes import Admin, Course, Student, Teacher
from api.tools.decorators import required_access
from api.tools.factory import error, response
from api.tools.google_storage import upload_blob

from . import admin


@admin.before_request
@required_access("Admin")
def admin_verification():
    # Required_access decorator already handled it
    pass


@admin.route("/add-teacher", methods=["GET", "POST"])
def add_teacher():
    """Adds a teacher account to the system.
    Returns
    -------
    dict
        Flashes, teacher data from the form
    """

    flashes = list()
    try:
        if not Teacher.get_by_email(request.form['email']):
            teacher = Teacher(
                request.form['email'],
                request.form['first_name'],
                request.form['last_name']
            )
            teacher.password(request.form['password'])
    except KeyError:
        return error("Not all fields satisfied."), 400

    if teacher.add():
        flashes.append("Teacher added!")
        logger.info(f"Teacher {teacher.email} added")
        token = teacher.get_activation_token()
        app = current_app._get_current_object()
        msg = Message(
            app.config["MAIL_SUBJECT_PREFIX"] + " " + "Account Activation Link",
            sender=app.config["MAIL_SENDER"],
            recipients=[teacher.email],
        )
        msg.body = f"""Here is your account activation link:
            { url_for('teacher.activate_account', token=token, _external=True) }
            If you did not register for this account, you can ignore this email. If you need any further assistance, please contact team@gradder.io.
            """
        mail.send(msg)        
        return response(flashes), 200
    else:
        logger.info(f"Error adding teacher {teacher.email}")
        flashes.append("There was a problem adding this account")
        return response(flashes), 400
        

@admin.route("/add-student", methods=["GET", "POST"])
def add_student():
    """Adds a student account to the system and sends an activation email.
    Returns
    -------
    dict
        Flashes, student data from the form
    """

    flashes = list()

    try:
        if not Student.get_by_email(request.form['email']):
            student = Student(
                request.form['email'],
                request.form['first_name'],
                request.form['last_name']
            )
            student.password(request.form['password'])
    except KeyError:
        return error("Not all fields satisfied"), 400
        
    if student.add():
        flashes.append("Student added!")
        logger.info(f"Student {student.email} added")
        token = current_user.get_activation_token()
        app = current_app._get_current_object()
        msg = Message(
            app.config["MAIL_SUBJECT_PREFIX"] + " " + "Account Activation Link",
            sender=app.config["MAIL_SENDER"],
            recipients=[student.email]
        )
        msg.body = f"""Here is your account activation link:
            { url_for('student.activate_account', token=token, _external=True) }
            If you did not register for this account, you can ignore this email. If you need any further assistance, please contact team@gradder.io.
            """
        mail.send(msg)        
        return response(flashes), 200
    else:
        logger.info(f"Error adding Student {student.email}")
        flashes.append("There was a problem adding this account"), 400
        return response(flashes), 400

@admin.route("/register-courses", methods=["GET", "POST"])
def register_courses():
    """Adds a course to the system.
    Returns
    -------
    dict
        Flashes, course data from the form
    """

    flashes = list()

    try:
        if Course.get_by_department_number(request.form['number']):
            course = Course(
                request.form['department'],
                request.form['number'],
                request.form['teacher'] if request.form['teacher'] else None,
                request.form['name'],
                request.form['description'],
                request.form['schedule_time'],
                request.form['schedule_days']
            )
    except KeyError:
        return error("Not all fields satisfied."), 400

    if Admin.add_course(course=course):
        logger.info(f"Course {request.form['number']} added")
        flashes.append("Course added!")
        return response(flashes), 200
    else:
        flashes.append("There was a problem adding your course")
        return response(flashes), 400
    
@admin.route("/add-student-to-course", methods=["GET", "POST"])
def add_student_to_course():
    """Adds a student to a course.
    Returns
    -------
    dict
        Flashes, student data from the form
    """

    flashes = list()

    try:
        if Student.get_by_email(request.form['email']):
            Admin.add_student(Course.get_by_department_number(request.form['number'])._id, request.form['email'])
        else:
            flashes.append("Account doesn't exist!")
            return response(flashes), 400

    except KeyError:
        return response(flashes), 400

@admin.route("/add-teacher-to-course", methods=["GET", "POST"])
def add_teacher_to_course():
    """Adds a teacher to a course.
    Returns
    -------
    dict
        Flashes, teacher data from the form
    """

    flashes = list()

    try:
        if Teacher.get_by_email(request.form['email']):
            Admin.add_teacher(Course.get_by_department_number(request.form['number'])._id, request.form['email'])
        else:
            flashes.append("Account doesn't exist!")
            return response(flashes), 400

    except KeyError:
        return response(flashes), 400

@admin.route("/course", methods=["GET"])
def manage_courses():
    """Returns a list of all courses in the school.
    Returns
    -------
    dict
        All course data
    """
    return response({"courses": Admin.get_courses()}), 200


@admin.route("/course/<string:course_id>", methods=["GET", "POST"])
def manage_courses_by_id(course_id: str):
    """Provides options to edit the course.
    Returns
    -------
    dict
        Flashes, course data from the form
    """
    
    flashes = list()

    course = Course.get_by_id(course_id)
    if course:
        if request.form.get('file'):
            syllabus_file = request.form['file']
            filename = syllabus_file.filename
            blob = upload_blob(
                uuid.uuid4().hex + "." + syllabus_file.content_type.split("/")[-1],
                syllabus_file,
            )
            syllabus = (blob.name, filename)
            course.update_syllabus(syllabus)
            logger.info(f"Course {course._id} updated")

        # NOTE: Possibly refactor this for Python 3.8 to be:
        """
        if (description := request.form.get('description')):
            course.update_description(description)
        
        # ... etc
        """
        if request.form.get('description'):
            course.update_description(request.form.get('description'))
        if request.form.get('grade_range'):
            course.update_grade_range(request.form.get('grade_range'))
        
        flashes.append("Course information successfully updated!")
        return response(flashes), 200
    else:
        return error("Course does not exist"), 404

@admin.route("/search", methods=["GET"])
def get_names_by_search():
    """Shows full names of people the user is searching
    Returns
    -------
    dict
        Admin names
    """
    try:
        admins = Admin.get_by_keyword(request.form['first_name'])
        possible_admins = list()
        for admin in admins:
            admin_data = {
                'full_name': admin.first_name + ' ' + admin.last_name,
            }
            possible_admins.append(admin_data)
        return response(data={"possible_admins": possible_admins}), 200
    except:
        return error("There are no admins by that name"), 404

@admin.route("/admin-search-info", methods=["GET", "POST"])
def admin_search_info():
    r"""This method is called when the user clicks on a result on the search bar
    Returns
    -------
    dict
        Flashes, admin data
    """
    try:
        return response(None, Admin.get_by_id(request.form['user_id'])), 200
    except:
        return error("There was a problem finding this user"), 404