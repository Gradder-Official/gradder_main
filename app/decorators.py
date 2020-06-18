from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user
from app.logs.user_logger import user_logger

def required_access(people):
    def iteration(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.USERTYPE not in people:
                flash("You do not have access to this page! Please check your login info.")
                return redirect(url_for('auth.login'))
            return func(*args, **kwargs)
        return decorated_function
    return iteration
