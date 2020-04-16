from flask import redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from .forms import ContactUsForm
from ..email import send_email
from . import main
from ..modules.db.classes.message import Message


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    from app import db

    form = ContactUsForm()

    if form.validate_on_submit():
        msg_id = db.collection_messages.document("last_message_id")
        new_id = str(int(msg_id.get().to_dict()["id"]) + 1)

        try:
            send_email(to=form.email.data.lower(), subject=f'Message #{ new_id }',
                template='contact_email_user', first_name=form.first_name.data, message=form.message.data, subject_msg=form.subject.data)
            
            print("First email sent!")

            send_email(to="team@gradder.io", subject=f'{ form.subject.data } | Message #{ new_id }',
                template='contact_email_admin', first_name=form.first_name.data, last_name=form.last_name.data, message=form.message.data, subject_msg=form.subject.data, message_id=new_id)

            msg_id.set({'id': new_id })

            db.add_message(Message(email=form.email.data.lower(), subject=form.subject.data, message=form.message.data, ID=msg_id.get().to_dict()["id"]))

        except BaseException as e:
            print(e)
            flash('Error while sending the message. Please try again')

    return render_template('contact.html', form=form)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/add-classes')
def add_classes():
    pass


@main.route('/view-classes')
def view_classes():
    pass


@main.route('/add-subjects')
def add_subjects():
    pass


@main.route('/new-auth-token')
def new_auth_token():
    pass


@main.route('/manage-school')
def manage_school():
    pass


@main.route('/view-assignments')
def view_assignments():
    pass


@main.route('/view-grades')
def view_grades():
    pass


@main.route('/add-children')
def add_children():
    pass


@main.route('/children_progress')
def children_progress():
    pass