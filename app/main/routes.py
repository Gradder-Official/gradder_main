import os
from datetime import datetime

from flask import redirect, url_for, render_template, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .forms import ContactUsForm, CareersForm, NewAssignmentForm
from ..email import send_email
from . import main
from ..modules.db.classes import Message, Application, Assignment, User, Student, Parent, Admin, Teacher
from app import db
from app.decorators import required_access
from app.logs.form_logger import form_logger

from google.cloud import storage

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactUsForm()

    if form.is_submitted():
        if form.validate():
            msg_id = db.collection_messages.document("last_message_id")
            new_id = str(int(msg_id.get().to_dict()["id"]) + 1)

            try:
                send_email(to=form.email.data.lower(), subject=f'Message #{ new_id }',
                           template='mail/contact_email_user', first_name=form.first_name.data, message=form.message.data, subject_msg=form.subject.data)

                send_email(to="team@gradder.io", subject=f'{ form.subject.data } | Message #{ new_id }',
                           template='mail/contact_email_admin', first_name=form.first_name.data,
                           last_name=form.last_name.data, message=form.message.data, subject_msg=form.subject.data, message_id=new_id)

                msg_id.set({'id': new_id})

                message = Message(email=form.email.data.lower(), subject=form.subject.data, first_name=form.first_name.data, last_name=form.last_name.data, message=form.message.data, ID=new_id)
                message.add()

            except BaseException as e:
                form_logger.exception("Email did not send")
                # flash('Error while sending the message. Please try again')
        else:
            pass
            # flash('Not valid input')

    return render_template('contact.html', form=form)


@main.route('/careers', methods=['GET', 'POST'])
def careers():
    form = CareersForm()

    form_logger.info("Form created")

    if form.validate_on_submit():
        f = form.resume.data
        if f is not None:
            form_logger.info("Form recieved")
            resume_filename = f.filename
            resume_content = f.read()

        old_id = db.collection_applications.document("last_application_id")
        new_id = str(int(old_id.get().to_dict()["id"]) + 1)

        try:
            form_logger.debug("Try entered")
            send_email(to=form.email.data.lower(), subject=f'We received your application!',
                       template='mail/careers_email_user', first_name=form.first_name.data, job=form.job.data, files=[(resume_filename, resume_content)] if f is not None else [], comments=form.comments.data)

            form_logger.info("Email sent")

            send_email(to="team@gradder.io", subject=f'Application #{new_id} | {form.job.data}',
                       template='mail/careers_email_admin', first_name=form.first_name.data,
                       last_name=form.last_name.data, job=form.job.data, email=form.email.data.lower(), ID=new_id, files=[(resume_filename, resume_content)] if f is not None else [], comments=form.comments.data)

            form_logger.info("Email sent")

            old_id.set({'id': new_id})

            # flash('Your application was received!')

            return redirect(url_for('main.index'))

        except BaseException as e:
            form_logger.exception("Email did not send")
            # flash('Error while sending the application. Please try again')

    return render_template('careers.html', form=form)


@main.route('/dashboard')
@login_required
def dashboard():
    curr_user = eval(current_user.USERTYPE.capitalize()).get_by_id(current_user.ID)

    if curr_user.USERTYPE == 'Student':
        return render_template('dashboard.html', assignments=curr_user.get_assignments())
    else:
        return render_template('dashboard.html')


@main.route('/teacher/add_assignment', methods=['GET', 'POST'])
@login_required
def add_assignment():
    form = NewAssignmentForm()

    if form.validate_on_submit():
        file_link_list = []
        for file in form.files.data:
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
        flash('Assignment created!')

    return render_template('add_assignment.html', form=form)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

def upload_blob(bucket_name, filename, file_obj):
    storage_client = storage.Client()
    bucket = storage_client.bucket('gradder-storage')
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj)
    form_logger.info('File {} uploaded'.format(filename))
    return blob