from flask import render_template, redirect, request, url_for, make_response
from flask_login import current_user
from app.modules.student.forms import SubmissionForm
from . import student
from ._student import Student
from app.modules._classes import Submission
from app.decorators import required_access
from datetime import datetime
from app.google_storage import upload_blob

@student.before_request
@required_access('Student')
def student_verification():
    # Required_access decorator already handled it
    pass


@student.route('/')
@student.route('/index')
@student.route('/dashboard')
def index():
    return render_template('student/dashboard.html', assignments=current_user.get_assignments())

@student.route('/submit', methods=["GET", "POST"])
def submit():
    form = SubmissionForm()
    if form.validate_on_submit():
        student = Student.get_by_id(current_user.ID)
        if request.files is not None:
            files = request.files.getlist(form.files.name)
            file_link_list = []
            for file_ in files:
                blob = upload_blob('gradder-storage', file_.filename, file_)
                file_link_list.append(blob.media_link)
        submission = Submission(date_submitted=datetime.utcnow(), comment=form.comment.data, file_links=file_link_list)
        student.add_submission("5efbe85b4aeb5d21e56fa81f", "5efdfc905bc672bf745e4580", submission=submission)
    return render_template('student/submission.html', form=form)

@student.route('/profile')
def profile():
    return render_template('student/profile.html')
