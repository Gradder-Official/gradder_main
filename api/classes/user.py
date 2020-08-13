from __future__ import annotations
from typing import Union, Dict, Optional
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
        description: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        profile_picture: Optional[str] = None,
        _id: Optional[str] = None,
        password: Optional[Union[str, bytes]] = None,
    ):
        r"""Init function for a generic User class.

        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        description : str, optional
        date_of_birth : str, optional
            The user's date of birth (dd-mm-yyyy), defaults to None if unspecified.
        profile_picture : str, optional
            Link to user's profile picture, defaults to None if unspecified.
        _id : str, optional
            The user's ID number, defaults to None if unspecified.
        password : str, optional
            The user's password. Defaults to None. If the password is not hashed, stores the hash.
        """
        self.email = email  # TODO: add validation (property)
        self.first_name = first_name  # TODO: add validation (property)
        self.last_name = last_name  # TODO: add validation (property)
        self.id = _id if _id is not None else ''
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
        if re.match(r"^\$2[ayb]\$.{56}$", str(password)):
            password = password if type(password) is bytes else password.encode("utf-8")
            self._password = password
        else:
            password = password if type(password) is bytes else password.encode("utf-8")
            self._password = hashpw(password, gensalt())

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = str(id)

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
        hashedPassword = hashpw(password.encode("utf-8"), gensalt())
        return checkpw(password.encode("utf-8"), hashedPassword)

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
    def from_dict(dictionary: dict) -> User:
        r"""Creates a new User object from the dictionary.
        """
        return User(**dictionary)

    @property
    def description(self) -> str:
        return self.description

    @description.setter
    def description(self, description: str):
        db.users.update({"id": self.id()}, {"$set": {"description": description}})

    @property
    def date_of_birth(self) -> str:
        return self.date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        date_format = '%d-%m-%Y'
        try:
            date_obj = datetime.datetime.strptime(date_string, date_format)
            db.users.update({"id": self.id()}, {"$set": {"date_of_birth": date_of_birth}})
        except ValueError:
            raise InvalidFormatException("Incorrect data format, should be DD-MM-YYYY")

    @property
    def profile_picture(self) -> str:
        return self.profile_picture
    
    @profile_picture.setter
    def profile_picture(self, profile_picture: str):
        return self.profile_picture

    def get_activation_token(self, expires_sec=1800):
        """Gets an activation token for a user

        Parameters
        ----------
        expires_sec : int
            Seconds before token expires, default to 1800

        Returns 
        ---------
        token : str 
            Token for activation
        """
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.ID}).decode("utf-8")

    @staticmethod
    def verify_activation_token(token:str):
        """Verifies the activation token for a user

        Parameters
        ----------
        token : str

        Returns 
        ---------
        User
        """
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.get_by_id(user_id)
