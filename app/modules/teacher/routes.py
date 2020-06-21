from datetime import datetime
from flask import redirect, url_for, flash, render_template, request
from flask_login import current_user
from werkzeug.utils import secure_filename

from . import teacher

from ._teacher import Teacher
from .forms import NewAssignmentForm

from app.decorators import required_access
from app.google_storage import upload_blob
from app.modules._classes import Assignment
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

    if form.validate_on_submit():
        files = request.files.getlist(form.files.name)
        file_link_list = []
        for file in files:
            blob = upload_blob('gradder-storage', file.filename, file)
            file_link_list.append(blob.media_link)
        
        new_assignment = Assignment(date_assigned=datetime.utcnow(),
                                    assigned_by=current_user.ID,
                                    assigned_to=form.assigned_to.data,
                                    due_by=form.due_by.data,
                                    subject=form.subject.data,
                                    content=form.content.data,
                                    file_links=file_link_list,
                                    estimated_time=form.estimated_time.data
                                    )
        new_assignment.add()
        flash('Assignment sent!')
        return redirect(url_for('main.dashboard'))

    return render_template('teacher/add_assignment.html', form=form)