from typing import Union, Dict
from future import __annotations__

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, email: str, first_name: str, last_name: str, _id: str = None):
        r"""Init function for a generic User class.

        Parameters
        ----------
        email: str
            The user's email
        first_name: str
            The user's first name
        last_name: str
            The user's last name
        _id: str, optional
            The user's ID number, defaults to None if unspecified.
        """
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self._id = _id
    
    def __repr__(self):
        return f"<User {self.ID}>"

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
    def from_dict(dictionary: dict) -> User:
        #TODO: the rest of the methods.