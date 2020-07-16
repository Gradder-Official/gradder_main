from functools import wraps
from flask import redirect, url_for, flash, abort
from flask_login import current_user
from app.logs.user_logger import user_logger

def required_access(people):
    def iteration(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.USERTYPE not in people:
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return iteration
