from functools import wraps

from flask import abort
from flask_login import current_user


def required_access(people: list):
    r"""Checks if current user has access to view a specific endpoint.
    The common use case is to put it after @[blueprint].before_request to check that every
    endpoint in a specific blueprint can be accessed only by the desired types of users.
    If the type of flask_login.current_user is not in people, raises the 403 forbidden error.
    Parameters
    ----------
    people: list
        The list of USERTYPES that can access a specific endpoint. Choose from ['Teacher', 'Student', 'Admin', 'Parent']
    """

    def iteration(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user._type not in people:
                abort(403)
            return func(*args, **kwargs)

        return decorated_function

    return iteration
