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
