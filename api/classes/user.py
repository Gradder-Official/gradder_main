from __future__ import annotations
from typing import Union, Dict
from bcrypt import hashpw, gensalt, checkpw

import re

from flask_login import UserMixin


class User(UserMixin):
    r"""The generic User class to be inherited by the others.

    Attributes
    ----------
    _password: str
        Protected password hash, use setter/getter for property __password__
    _id: str
        Protected ID property, use setter/getter for property __id__
    _type: str
        Stores the type of the current user (one of the types in tools.dictionaries.TYPE_DICTIONARY), immutable

    email: str
    first_name: str
    last_name: str

    Notes
    -----
    Do not use a User object directly, this is a generic object that should be inherited by more specific user classes.
    """
    _type: str = None

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        _id: str = None,
        password: str = None,
    ):
        r"""Init function for a generic User class.

        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        _id : str, optional
            The user's ID number, defaults to None if unspecified.
        password : str, optional
            The user's password. Defaults to None. If the password is not hashed, stores the hash.
        """
        self.email = email  # TODO: add validation (property)
        self.first_name = first_name  # TODO: add validation (property)
        self.last_name = last_name  # TODO: add validation (property)
        self._id = _id
        self.password = password if password is not None else ''

    def __repr__(self):
        return f"<User {self._id}>"

    @property
    def password(self) -> str:
        r"""Returns the hash of the password.
        """
        return self._password

    @password.setter
    def password(self, password: str):
        r"""The setter method for the password.
        
        Parameters
        ----------
        password : str
            The new password. If the password is a valid hash, will set it to this value (otherwise, will set it to the hash of the new password).
        """

        # If a password is already a valid hash
        if re.match(r"^\$2[ayb]\$.{56}$", password):
            password = password.encode("utf-8")
            self._password = password
        else:
            password = password.encode("utf-8")
            self._password = hashpw(password, gensalt())

    def validate_password(self, password: str) -> bool:
        r"""Validates a password against the previously set hash.

        Parameters
        ----------
        password : str
            The password to validate against the hash of the user.

        Returns
        -------
        bool
            `True` if the password is valid, `False` otherwise.
        """
        return checkpw(password, self.password)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        r"""Sets the id for the user.

        Parameters
        ----------
        id : str
            The new ID.
        """
        self._id = id

    def to_dict(self) -> Dict[str, str]:
        r"""Converts the object to a dictionary.
        """
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
        }

    @staticmethod
    def from_dict(dictionary: dict) -> 'User':
        r"""Creates a new User object from the dictionary.
        """
        return User(**dictionary)
