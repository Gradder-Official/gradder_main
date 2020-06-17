from flask import render_template, redirect, url_for, request

from . import parent
from ._parent import Parent

from app.decorators import required_access

@parent.before_request
@required_access('Parent')
def parent_verification():
    # Required_access decorator already handled it
    pass


@parent.route('/')
@parent.route('/index')
@parent.route('/dashboard')
def index():
    return render_template('parent/dashboard.html')


@parent.route('/profile')
def profile():
    return render_template('parent/profile.html')