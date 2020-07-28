from typing import Union

from flask import redirect, current_app, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse

from api import db, login_manager
from api.classes import User, Teacher, Student, Admin, Parent
from api.tools.factory import response, error

from api.tools.dictionaries import TYPE_DICTIONARY

from . import auth
from .forms import LoginForm, ResetPasswordForm, PasswordChangeForm


@login_manager.user_loader
def load_user(id: str) -> Union[Teacher, Student, Parent, Admin]:
    """User loader function used by Flask-Login.

    Important: this is not an endpoint, and therefore the return is not JSON-valid.

    Parameters
    ----------
    id: str
        The ID to look up in the database.

    Returns
    -------
    Union[Teacher, Student, Parent, Admin]
        The user object that was retrieved from the database. Will return None if no users with a specified ID can be found.
    """
    user = None
    for scope in [Teacher, Student, Admin, Parent]:
        user = scope.get_by_id(id)
        if user is not None:
            break
    
    if user is not None:
        return TYPE_DICTIONARY[user["usertype"]].from_dict(user)

    return None


@auth.route("/login", methods=["POST"])
def login():
    """Login endpoint. Handles user logins with LoginForm

    Returns
    -------
    dict
        The view response
    """
    
    if current_user.is_authenticated:
        # TODO: Redirect to dashboard
        return error("Already authenticated")

    form = LoginForm()
    if form.validate_on_submit():
        # TODO: Get user
        user = User.get_by_email(form.email.data.lower())
        if user is not None:
            user = TYPE_DICTIONARY[user["usertype"].capitalize()].from_dict(user)
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
            else:
                return error("Email or password is incorrect")

            # TODO: Log the authentication
        return response(["Logged in successfully"])

    return response(forms={"login": form})


@auth.route("/logout")
@login_required
def logout():
    """Logout the user

    Returns
    -------
    dict
        The view response
    """
    # TODO: Log the de-authentication
    logout_user()
    return response(["You have been logged out"])


@auth.route("/change-password", methods=["POST"])
@login_required
def change_password():
    form = PasswordChangeForm()
    user = TYPE_DICTIONARY[
        current_user.USERTYPE.capitalize()].get_by_id(current_user.ID)
    
    if form.validate_on_submit():
        pass

@auth.route("/request-password-reset", methods=["POST"])
def request_password_reset():
    pass

@auth.route("/request-password-reset/<token:string>", methods=["POST"])
def password_reset(token: str):
    pass
