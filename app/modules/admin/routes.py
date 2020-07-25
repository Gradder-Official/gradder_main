from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user
import uuid

from bson import ObjectId
from app import db
from app.logger import logger
from app.decorators import required_access
from app.modules._classes import Classes
from app.google_storage import upload_blob

from . import admin
from ._admin import Admin
from .forms import (
    NewStudentsTeachers,
    NewClasses,
    AddStudentClass,
    AddTeacherClass,
    EditClassForm,
)


@admin.before_request
@required_access("Admin")
def admin_verification():
    # Required_access decorator already handled it
    pass


@admin.route("/")
@admin.route("/index")
@admin.route("/dashboard")
def index():
    return render_template("admin/dashboard.html")


@admin.route("/profile")
def profile():
    return render_template("admin/profile.html")


@admin.route("/registerTS", methods=["GET", "POST"])
def registerTS():
    # Method adds new Teachers/Students
    flashes = list()
    form = NewStudentsTeachers()
    if form.validate_on_submit():
        user = eval(
            f"{form.user_type.data}(email=form.email.data.lower(), first_name=form.first_name.data, last_name=form.last_name.data)"
        )

        user.set_password(form.password.data)
        user.set_secret_question(
            question=form.secret_question.data, answer=form.secret_answer.data.lower()
        )
        if user.add():
            db.delete_auth_token(form.auth_token.data)
            logger.info(
                "NEW USER: {} {} {} - ACCESS: {}".format(
                    user.first_name, user.last_name, user.email, user.USERTYPE
                )
            )
            logger.info(
                "NEW USER: {} {} {} - ACCESS: {}".format(
                    user.first_name, user.last_name, user.email, user.USERTYPE
                )
            )
            flashes.append("New Teacher/Student has been added")
            return redirect(url_for("auth.login"))
        else:
            logger.error(
                "Unknown error while registering: {} {} {} - ACCESS: {}".format(
                    user.first_name, user.last_name, user.email, user.USERTYPE
                )
            )
            logger.error(
                "Unknown error while registering: {} {} {} - ACCESS: {}".format(
                    user.first_name, user.last_name, user.email, user.USERTYPE
                )
            )
            flashes.append("Unknown error while registering.")

    return {
        'forms': {
            'new_ts': form.get_form_json()
        },
        'flashes': flashes,
        'data': {
            'first_name': form.first_name,
            'last_name': form.last_name,
            'email': form.email
        }
    }


@admin.route("/registerClasses", methods=["GET", "POST"])
def registerClasses():
    register_classes = NewClasses()
    flashes = list()
    if register_classes.validate_on_submit():
        new_class = Classes(
            department=register_classes.department.data,
            number=register_classes.number.data,
            name=register_classes.name.data,
            teacher=ObjectId(register_classes.teacher.data),
            description=register_classes.description.data,
            schedule_time=register_classes.schedule_time.data,
            schedule_days=register_classes.schedule_days.data,
        )

        Admin.add_class(new_class)

        logger.info(
            "NEW CLASS: {} {} {} ".format(
                new_class.name, new_class.teacher, new_class.description
            )
        )
        flashes.append(
            "New Class has been added to DB!"
        )
    # I think this is right feel free to comment it if it isn't correct
    return {
        'forms': {
            'register_class': register_classes.get_form_json()
        },
        'flashes': flashes,
        'data': {
            'department': new_class.department,
            'number': new_class.number,
            'name': new_class.name,
            'teacher': new_class.teacher,
            'description': new_class.description,
            'schedule_time': new_class.schedule_time,
            'schedule_days': new_class.schedule_days
        }
    }

    # return render_template("admin/register.html", form=form)


@admin.route("/studentClass", methods=["GET", "POST"])
def addStudentClass():
    add_student_form = AddStudentClass()
    if add_student_form.validate_on_submit():
        Admin.add_student(add_student_form.class_id.data, add_student_form.email.data)
        logger.info(
            "NEW STUDENT IN: {}  - STUDENT EMAIL: {}".format(
                add_student_form.class_id.data, add_student_form.email.data
            )
        )
        logger.info(
            "NEW STUDENT IN: {}  - STUDENT EMAIL: {}".format(
                add_student_form.class_id.data, add_student_form.email.data
            )
        )
    else:
        logger.error(
            "Error in registering NEW STUDENT IN: {}  - STUDENT EMAIL: {}".format(
                add_student_form.class_id.data, add_student_form.email.data
            )
        )
        logger.error(
            "Error in registering NEW STUDENT IN: {}  - STUDENT EMAIL: {}".format(
                add_student_form.class_id.data, add_student_form.email.data
            )
        )
    return {
        'forms': {
            'add_student': add_student_form.get_form_json()
        },
        'flashes': [],
        'data': []
    }


@admin.route("/teacherClass", methods=["GET", "POST"])
def addTeacherClass():
    add_teacher_form = AddTeacherClass()
    if add_teacher_form.validate_on_submit():
        Admin.add_teacher(add_teacher_form.class_id.data, add_teacher_form.email.data)
        logger.info(
            "NEW TEACHER IN: {}  - TEACHER EMAIL: {}".format(
                add_teacher_form.class_id.data, add_teacher_form.email.data
            )
        )
        logger.info(
            "NEW TEACHER IN: {}  - TEACHER EMAIL: {}".format(
                add_teacher_form.class_id.data, add_teacher_form.email.data
            )
        )
    else:
        logger.error(
            "Error in registering NEW TEACHER IN (Class Id: {}) - TEACHER EMAIL is: {}".format(
                add_teacher_form.class_id.data, add_teacher_form.email.data
            )
        )
        logger.error(
            "Error in registering NEW TEACHER IN (Class Id: {}) - TEACHER EMAIL is: {}".format(
                add_teacher_form.class_id.data, add_teacher_form.email.data
            )
        )
    return {
        'forms': {
            'add_teacher': add_teacher_form.get_form_json()
        },
        'flashes': [],
        'data': []
    }

@admin.route("/class", methods=["GET"])
def manage_classes():
    try:
        classes = current_user.get_class_names()
    except TypeError:
        # We can assume that the admin has no classes.
        classes = []

    classes = list(map(lambda class_: [str(class_[0]), class_[1]], classes))

    return {
        'forms': {
            'edit_class': EditClassForm().get_form_json()
        },
        'flashes': [],
        'data': {
            'classes': classes
        }
    }

@admin.route("/class/<string:class_id>", methods=["GET", "POST"])
def manage_classes_by_id(class_id: str):
    flashes = []
    class_edit_form = EditClassForm()
    class_ = Classes.get_by_id(class_id)

    syllabus_name = class_.get_syllabus_name()
    if syllabus_name is not None:
        if len(syllabus_name) > 20:
            syllabus_name = syllabus_name[:20] + "..."
        class_edit_form.syllabus.label.text = (
            f"Update syllabus (current: { syllabus_name })"
        )

    if class_edit_form.validate_on_submit():
        syllabus = tuple()
        if class_edit_form.syllabus.name is not None:
            syllabus_file = request.files[class_edit_form.syllabus.name]
            filename = syllabus_file.filename
            blob = upload_blob(
                uuid.uuid4().hex + "." + syllabus_file.content_type.split("/")[-1],
                syllabus_file,
            )
            syllabus = (blob.name, filename)
            logger.info("Specific Id Class: {}".format(class_))

        class_.update_description(class_edit_form.description.data)
        class_.update_syllabus(syllabus)

        flashes.append(
            "Class information successfully updated!"
        )

    try:
        classes = current_user.get_class_names()
    except TypeError:
        # We can assume that the admin has no classes.
        classes = []

    classes = list(map(lambda class_: [str(class_[0]), class_[1]], classes))

    return {
        'forms': {
            'class_edit': EditClassForm().get_form_json()
        },
        'flashes': flashes,
        'data': {
            'current_description': class_.description,
            'class_json': class_.to_dict(),
            'classes': classes,
        }
    }


# @admin.route('/students', methods=['GET', 'POST'])
# def allStudents():
#     form = AddTeacherClass()
#     if form.validate_on_submit():
#         Admin.add_teacher(form.class_id.data, form.email.data)
#     return render_template('admin/register.html', form=form)
