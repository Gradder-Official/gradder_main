from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from .forms import LoginForm, RegistrationForm
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
            print(current_user.is_authenticated)
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
        user = eval(f'{form.user_type.data}(email=form.email.data.lower(), first_name=form.first_name.data, last_name=form.last_name.data)')

        user.set_password(form.password.data)

        if db.add_user(user):
            db.delete_auth_token(form.auth_token.data)
            return redirect(url_for('auth.login'))
        else:
            flash('Unknown error while registering.')
    
    return render_template('auth/register.html', form=form)