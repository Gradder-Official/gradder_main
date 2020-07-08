from datetime import datetime
from flask import redirect, url_for, flash, render_template, request
from flask_login import current_user
from werkzeug.utils import secure_filename

from . import admin

from ._admin import Admin
from app.modules._classes import Classes

from app.decorators import required_access
from app.google_storage import upload_blob
from app.modules._classes import Assignment, Classes
from app.logs.form_logger import form_logger
import uuid
# from app.modules.admin._admin import add_student

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
    # add_student("912f58eccfe825c85801", "coolgm@gmail.com")
    return render_template('admin/profile.html')


# @admin.route('/class', methods=['GET'])
# def manage_classes():
#     return redirect(url_for('admin.manage_classes_by_id', class_id=current_user.get_class_names()[0][0]))

# @admin.route('/class/<string:class_id>', methods=['GET'])
# def manage_classes_by_id(class_id: str):
#     return render_template('/admin/manage_classes.html', classes=current_user.get_class_names(), class_json=Classes.get_by_id(class_id).to_json())