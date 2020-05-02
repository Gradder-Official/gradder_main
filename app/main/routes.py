import os

from flask import redirect, url_for, render_template, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .forms import ContactUsForm, CareersForm
from ..email import send_email
from . import main
from ..modules.db.classes import Message, Application


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    from app import db

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

                db.add_message(Message(email=form.email.data.lower(
                ), subject=form.subject.data, first_name=form.first_name.data, last_name=form.last_name.data, message=form.message.data, ID=new_id))

            except BaseException as e:
                print(e)
                # flash('Error while sending the message. Please try again')
        else:
            pass
            # flash('Not valid input')

    return render_template('contact.html', form=form)


@main.route('/careers', methods=['GET', 'POST'])
def careers():
    from app import db

    form = CareersForm()

    print("Form created")

    if form.validate_on_submit():
        f = form.resume.data
        if f is not None:
            print('File received')
            resume_filename = f.filename
            resume_content = f.read()

        old_id = db.collection_applications.document("last_application_id")
        new_id = str(int(old_id.get().to_dict()["id"]) + 1)

        try:
            print("Try in")
            send_email(to=form.email.data.lower(), subject=f'We received your application!',
                       template='mail/careers_email_user', first_name=form.first_name.data, job=form.job.data, files=[(resume_filename, resume_content)] if f is not None else [], comments=form.comments.data)

            print("Email sent")

            send_email(to="team@gradder.io", subject=f'Application #{new_id} | {form.job.data}',
                       template='mail/careers_email_admin', first_name=form.first_name.data,
                       last_name=form.last_name.data, job=form.job.data, email=form.email.data.lower(), ID=new_id, files=[(resume_filename, resume_content)] if f is not None else [], comments=form.comments.data)

            print("Email sent")

            old_id.set({'id': new_id})

            # flash('Your application was received!')

            return redirect(url_for('main.index'))

        except BaseException as e:
            print(e)
            # flash('Error while sending the application. Please try again')

    return render_template('careers.html', form=form)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/teacher/add-classes')
def add_classes():
    return redirect(url_for('index'))


@main.route('/view-classes')
def view_classes():
    return redirect(url_for('index'))


@main.route('/add-subjects')
def add_subjects():
    return redirect(url_for('index'))


@main.route('/new-auth-token')
def new_auth_token():
    return redirect(url_for('index'))


@main.route('/manage-school')
def manage_school():
    return redirect(url_for('index'))


@main.route('/view-assignments')
def view_assignments():
    return redirect(url_for('index'))


@main.route('/view-grades')
def view_grades():
    return redirect(url_for('index'))


@main.route('/add-children')
def add_children():
    return redirect(url_for('index'))


@main.route('/children_progress')
def children_progress():
    return redirect(url_for('index'))
