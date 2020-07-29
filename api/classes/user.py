from typing import Union, Dict
from future import __annotations__
from bcrypt import hashpw, gensalt, checkpw

from flask_login import UserMixin


class User(UserMixin):
    _password: str
    _id: str
    email: str
    first_name: str
    last_name: str

    def __init__(self, email: str, first_name: str, last_name: str, _id: str = None, password: str = None):
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
        password: str, optional
            The user's password. Defaults to None. If the password is not hashed, stores the hash.
        """
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self._id = _id
        self.set_password(password)
    
    def __repr__(self):
        return f"<User {self.ID}>"

    @property
    def pasword(self) -> str:
        return self._password
        
    @password.setter
    def password(self, password: str):
        # If a password is already a valid hash
        if (re.match(r"^\$2[ayb]\$.{56}$", password)):
            self.password_hash = password
        else:
            self.password_hash = hashpw(password, gensalt())
    
    def validate_password(self, password: str) -> bool:
        return checkpw(password, self.password)

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
        return User(**dictionary)