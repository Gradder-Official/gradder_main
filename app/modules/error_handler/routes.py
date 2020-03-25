from flask import render_template
from . import error_handler

@error_handler.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@error_handler.errorhandler(500)
def internal_server_eror(e):
    return render_template('500.html'), 500