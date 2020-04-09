from flask import redirect, url_for, render_template
from flask_login import login_required, current_user
from . import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/features')
def features():
    return render_template('features.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


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