import uuid
import tempfile
import webbrowser
import os
from flask import render_template, redirect, request, url_for, make_response
from flask_login import current_user
from app.modules.teacher.forms import NewSubmissionForm
from . import student
from ._student import Student
from app.modules._classes import Submission
from app.decorators import required_access
from datetime import datetime
from app.google_storage import upload_blob, download_blob_binary, download_blob
from app import db
from bson import ObjectId


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

@student.route('/submit/<class_id>/<assignment_id>', methods=["GET", "POST"])
def submit(class_id, assignment_id):
    form = NewSubmissionForm()
    assignment = db.classes.find_one({"assignments._id": ObjectId(assignment_id)}, {"_id": 0, "assignments": {"$elemMatch": {"_id": ObjectId(assignment_id)}}})["assignments"][0]
    full_name = current_user.first_name + " " +  current_user.last_name
    content = assignment["content"]
    estimated_time = assignment["estimated_time"]
    due_by = assignment["due_by"]
    if form.validate_on_submit():
        student = Student.get_by_id(current_user.ID)
        file_list = []
        files = request.files.getlist(form.files.name)
        if files[0].filename:
            for file_ in files:
                filename = file_.filename
                blob = upload_blob(uuid.uuid4().hex + "." + file_.content_type.split("/")[-1], file_)
                file_list.append((blob.name, filename))
        submission = Submission(date_submitted=datetime.utcnow(), content=form.content.data, filenames=file_list)
        student.add_submission(current_user.ID, class_id, assignment_id, submission=submission) # need to replace IDs with current class and assignment ID
    return render_template('student/submission.html', form=form, class_id=class_id, assignment_id=assignment_id, full_name=full_name, 
                        content=content, estimated_time=estimated_time, due_by=due_by)

@student.route('/profile')
def profile():
    return render_template('student/profile.html')
    

@student.route('/assignments')
def assignments():
    print(list(map(lambda x: x.to_json(), current_user.get_assignments())))
    return render_template('student/assignments.html', assignments=list(map(lambda x: x.to_json(), current_user.get_assignments())))

@student.route('/view_assignment/<filename>/<real_filename>', methods=['GET', 'POST'])
def view_assignment(filename, real_filename):
    blob = download_blob_binary(filename, real_filename)
    with tempfile.TemporaryDirectory() as temp_dir:
        print(temp_dir)
        temp_file_path = os.path.join(temp_dir, filename)

        # write a normal file within the temp directory
        with open(temp_file_path, 'wb+') as fh:
            fh.write(blob)

        webbrowser.open('file://' + temp_file_path)
    return 'OK'