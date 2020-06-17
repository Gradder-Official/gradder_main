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
<<<<<<< HEAD
                return redirect(url_for('auth.login'))
=======
                user_logger.info("{} {} {} ACCESS - {} tried to access a restricted page".format(
                    current_user.first_name, current_user.last_name, current_user.email, current_user.USERTYPE))
                return redirect(url_for('auth.login'))
            else:
                pass
>>>>>>> dev
            return func(*args, **kwargs)
        return decorated_function
    return iteration
