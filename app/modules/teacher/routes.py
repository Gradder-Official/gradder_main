from datetime import datetime
from flask import redirect, url_for, flash, render_template, request
from flask_login import current_user
from werkzeug.utils import secure_filename

from . import teacher

from ._teacher import Teacher
from app.modules._classes import Classes
from .forms import NewAssignmentForm

from app.decorators import required_access
from app.google_storage import upload_blob
from app.modules._classes import Assignment, Classes
from app.logs.form_logger import form_logger


@teacher.before_request
@required_access('Teacher')
def teacher_verification():
    # Required_access decorator already handled it
    pass


@teacher.route('/')
@teacher.route('/index')
@teacher.route('/dashboard')
def index():
    return render_template('teacher/dashboard.html')


@teacher.route('/profile')
def profile():
    return render_template('teacher/profile.html')



@teacher.route('/add_assignment', methods=['GET', 'POST'])
def add_assignment():
    form = NewAssignmentForm()

    form.assigned_to.choices = current_user.get_class_names()

    if form.validate_on_submit():
        file_link_list = []
        if request.files is not None:
            files = request.files.getlist(form.files.name)
            for file_ in files:
                blob = upload_blob('gradder-storage', file_.filename, file_)
                file_link_list.append(blob.media_link)
        
        new_assignment = Assignment(date_assigned=datetime.utcnow(),
                                    assigned_by=current_user.ID,
                                    assigned_to=form.assigned_to.data,
                                    due_by=form.due_by.data,
                                    content=form.content.data,
                                    file_links=file_link_list,
                                    estimated_time=form.estimated_time.data
                                    )
        
        Classes.get_by_id(form.assigned_to.data).add_assignment(new_assignment)

        flash('Assignment sent!')
        return redirect(url_for('main.dashboard'))

    return render_template('teacher/add_assignment.html', form=form)

@teacher.route('/class', methods=['GET'])
def manage_classes():
    return redirect(url_for('teacher.manage_classes_by_id', class_id=current_user.get_class_names()[0][0]))

@teacher.route('/class/<string:class_id>', methods=['GET'])
def manage_classes_by_id(class_id: str):
    return render_template('/teacher/manage_classes.html', classes=current_user.get_class_names(), class_json=Classes.get_by_id(class_id).to_json())