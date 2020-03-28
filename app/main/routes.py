from flask import redirect, url_for, render_template
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
