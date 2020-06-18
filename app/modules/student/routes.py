from flask import render_template, redirect, request, url_for, make_response
from flask_login import current_user

from . import student
from ._student import Student

from app.decorators import required_access

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

@student.route('/profile')
def profile():
    return render_template('student/profile.html')