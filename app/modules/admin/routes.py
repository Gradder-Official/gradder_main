from flask import render_template, redirect, request, url_for
from . import admin
from ._admin import Admin
from app.decorators import required_access

@admin.before_request
@required_access('Admin')
def admin_verification():
    # Required_access decorator already handled it
    pass


@admin.route('/')
@admin.route('/index')
@admin.route('/dashboard')
def index():
    return render_template('admin/dashboard.html')


@admin.route('/profile')
def profile():
    return render_template('admin/profile.html')