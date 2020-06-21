from datetime import datetime 

from flask import render_template, redirect, request, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message

from app import db, login_manager

from . import auth

from .forms import LoginForm, RegistrationForm, PasswordChangeForm, SecretQuestionChangeForm, RequestResetForm, ResetPasswordForm
from app import mail
from app.modules._classes import User
from app.modules.teacher._teacher import Teacher
from app.modules.student._student import Student
from app.modules.admin._admin import Admin
from app.modules.parent._parent import Parent

from app.logs.user_logger import user_logger

@login_manager.user_loader
def load_user(id: str):
    user = User.get_by_id(id)
    if user is not None:
        return eval(user['usertype'].capitalize()).from_dict(user)
    else:
        return None


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data.lower())
        user = eval(user['usertype'].capitalize()).from_dict(user)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            
            user_logger.info("{} LOGGED IN: {} {} {} - ACCESS: {}".format(datetime.utcnow(), user.first_name, user.last_name, user.email, user.USERTYPE))

            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.dashboard')

            return redirect(next)
        flash('Invalid email or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = eval(
            f'{form.user_type.data}(email=form.email.data.lower(), first_name=form.first_name.data, last_name=form.last_name.data)')

        user.set_password(form.password.data)
        user.set_secret_question(question=form.secret_question.data, answer=form.secret_answer.data.lower())

        if user.add():
            db.delete_auth_token(form.auth_token.data)
            user_logger.info("NEW USER: {} {} {} - ACCESS: {}".format(user.first_name, user.last_name, user.email, user.USERTYPE))
            return redirect(url_for('auth.login'))
        else:
            user_logger.error("Unknown error while registering: {} {} {} - ACCESS: {}".format(user.first_name, user.last_name, user.email, user.USERTYPE))
            flash('Unknown error while registering.')

    return render_template('auth/register.html', form=form)


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = PasswordChangeForm()

    curr_user = eval(current_user.USERTYPE).get_by_id(current_user.ID)  #  Pull the user from the DB, as the current user is not updated

    form.secret_question.label.text += f' ({curr_user.secret_question})'

    if form.validate_on_submit():
        if curr_user.verify_secret_question(form.secret_question.data.lower()):
            curr_user.set_password(form.new_password.data)

            if curr_user.add():
                return redirect(url_for('main.profile'))
            else:
                flash('Unknown error while changing the password.')
                return render_template('auth/change-password.html', form=form)

        flash('Oops... Answer to the secret question is wrong.')

    return render_template('auth/change-password.html', form=form)

def send_reset_email(user):
    token = user.get_reset_token()
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + 'Password Reset Link',
                  sender=app.config['MAIL_SENDER'], recipients=[user.email])
    msg.body = f'''Here is your password reset link:
{ url_for('auth.reset_password', token=token, _external=True) }

If you did not make this reset password request, please change your password immediately through your accounts. If you need any further assistance, please contact team@gradder.io.
'''
    mail.send(msg)

@auth.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset(): 
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RequestResetForm()
    if form.validate_on_submit():
        send_reset_email(User.from_dict(User.get_by_email(form.email.data)))
        flash('An email has been sent to reset your password.')
        return redirect(url_for('auth.login'))
    return render_template('auth/send-reset-password.html', form=form)

@auth.route('/request-password-reset/<token>', methods=['GET', 'POST'])
def reset_password(token): 
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an expired or incorrect link.')
        return redirect(url_for('auth.reset_password_request'))
    user = User.from_dict(user)
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.update_password(form.new_password.data)
        flash('Password was successfully reset.')
        return redirect(url_for('main.dashboard'))
    return render_template('auth/reset-password.html', form=form)


@auth.route('/change-secret-question', methods=['GET', 'POST'])
@login_required
def change_secret_question():
    form = SecretQuestionChangeForm()

    curr_user = eval(current_user.USERTYPE).get_by_id(current_user.ID)  # Pull the user from the DB, as the current user is not updated
    if form.validate_on_submit():
        if curr_user.verify_password(form.password.data):
            curr_user.set_secret_question(form.new_secret_question.data, form.new_secret_answer.data.lower())

            if curr_user.add():
                return redirect(url_for('main.profile'))
            else:
                flash('Unknown error while changing the secret question.')
                return render_template('auth/change-secret-question.html', form=form)
            
        flash('Oops... Wrong password.')

    return render_template('auth/change-secret-question.html', form=form)

