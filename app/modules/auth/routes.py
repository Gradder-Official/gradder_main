from flask import render_template, redirect, request, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from .forms import LoginForm, RegistrationForm, PasswordChangeForm, SecretQuestionChangeForm
from app.modules.db.classes import Admin, Teacher, Student, Parent


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous():
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    from app import db
    form = LoginForm()
    if form.validate_on_submit():
        user = db.get_user_by_email(form.email.data.lower())
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
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
    from app import db
    form = RegistrationForm()
    if form.validate_on_submit():
        user = eval(
            f'{form.user_type.data}(email=form.email.data.lower(), first_name=form.first_name.data, last_name=form.last_name.data)')

        user.set_password(form.password.data)
        user.set_secret_question(question=form.secret_question.data, answer=form.secret_answer.data.lower())

        if db.add_user(user):
            db.delete_auth_token(form.auth_token.data)
            return redirect(url_for('auth.login'))
        else:
            flash('Unknown error while registering.')

    return render_template('auth/register.html', form=form)


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    from app import db

    form = PasswordChangeForm()

    curr_user = db.get_user_by_id(current_user.to_dict()['ID'])  #  Pull the user from the DB, as the current user is not updated
    print(curr_user.to_dict())

    if form.validate_on_submit():
        if curr_user.verify_secret_question(form.secret_question.data.lower()):
            curr_user.set_password(form.new_password.data)

            if db.add_user(curr_user):
                return redirect(url_for('main.profile'))
            else:
                flash('Unknown error while changing the password.')
                return render_template('auth/change_password.html', form=form)

        flash('Oops... Answer to the secret question is wrong.')

    return render_template('auth/change-password.html', form=form, secret_question=curr_user.secret_question)


@auth.route('/change-secret-question', methods=['GET', 'POST'])
@login_required
def change_secret_question():
    from app import db

    form = SecretQuestionChangeForm()

    curr_user = db.get_user_by_id(current_user.to_dict()['ID'])  # Pull the user from the DB, as the current user is not updated
    if form.validate_on_submit():
        if curr_user.verify_password(form.password.data):
            curr_user.set_secret_question(form.new_secret_question.data, form.new_secret_answer.data.lower())

            if db.add_user(curr_user):
                return redirect(url_for('main.profile'))
            else:
                flash('Unknown error while changing the secret question.')
                return render_template('auth/change-secret-question.html', form=form)
            
        flash('Oops... Wrong password.')

    return render_template('auth/change-secret-question.html', form=form)
