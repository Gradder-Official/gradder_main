from __future__ import annotations
from typing import Union, Dict, Optional
from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin
from bson import ObjectId
import datetime
import re

from api.tools.exceptions import InvalidTypeException, InvalidFormatException


class User(UserMixin):
    r"""The generic User class to be inherited by the others.

    Attributes
    ----------
    #TODO: add documentation here

    Notes
    -----
    Do not use a User object directly, this is a generic object that should be inherited by more specific user classes.
    """
    _type: str = None

    _id: str
    _password: bytes
    _email: str
    _first_name: str
    _last_name: str
    _bio: str
    _date_of_birth: str
    _profile_picture: str

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        bio: Optional[str] = None,
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
        bio : str, optional
        date_of_birth : str, optional
            The user's date of birth (dd-mm-yyyy), defaults to None if unspecified.
        profile_picture : tuple, optional
            Link to user's profile picture, defaults to empty tuple if unspecified.
        _id : str, optional
            The user's ID number, defaults to None if unspecified.
        password : str, optional
            The user's password. Defaults to None. If the password is not hashed, stores the hash.
        """
        self.email = email  # TODO: add validation (property)
        self.first_name = first_name  # TODO: add validation (property)
        self.last_name = last_name  # TODO: add validation (property)
        self.password = password or ""
        self.bio = bio or ""
        self.date_of_birth = date_of_birth or ""
        self.profile_picture = profile_picture or ""
        if _id is not None:
            self.id = _id

    def __repr__(self):
        return f"<User {self.id}>"

    def to_dict(self) -> Dict[str, str]:
        r"""Converts the object to a dictionary.
        """
        dictionary = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
        }

        try:
            dictionary["_id"] = self.id
        except:
            logger.info("This user has not been initialized yet.")

        return dictionary

    @classmethod
    def from_dict(cls, dictionary: dict) -> User:
        r"""Creates a new User object from the dictionary.
        """
        return cls(**dictionary)

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        if not isinstance(email, str):
            raise InvalidTypeException(
                f"The email provided is not a str (type provided is {type(email)})."
            )
        
        if not re.match(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email):
            raise InvalidFormatException(f"The email given is not in a valid email format (got {email})")

        self._email = email

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        # TODO: validation here
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        # TODO: validation here
        self._last_name = last_name

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
    def id(self, id: Union[ObjectId, str]):
        if not isinstance(id, (ObjectId, str)):
            raise InvalidTypeException(
                f"The id provided is not a str or bson.objectid.ObjectId (type provided is {type(id)})."
            )

        try:
            if isinstance(id, str):
                ObjectId(id)
            else:
                id = str(id)
        except Exception as e:
            raise InvalidFormatException(
                f"Cannot convert provided id to bson.ObjectId: {e}"
            )

        self._id = id

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
        return checkpw(password.encode("utf-8"), self.password)

    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, bio: str):
        if not isinstance(bio, str):
            raise InvalidTypeException(
                f"The bio provided is not a str (type provided is {type(bio)})."
            )

        if bio == "":
            self._bio = "A short bio."
            return

        if not 0 < len(bio) <= 100:
            raise InvalidFormatException(
                f"The string provided is too long. The bio should not exceed 100 characters. (currently: {len(bio)})"
            )

        if not re.match(
            r'[\w \.\+\(\)\[\]\{\}\?\*\&\^\%\$\#\/\'"~<>,:;!-_=@]{1,100}',
            bio,
            flags=re.UNICODE,
        ):
            raise InvalidFormatException(
                r"The format for bio doesn't match. Expected '[\w \.\+\(\)\[\]\{\}\?\*\&\^\%\$\#\/\'\"~<>,:;!-_=@]{1, 500}', got {bio}".format(
                    bio=bio
                )
            )

        self._bio = bio

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        date_format = "%d-%m-%Y"
        if not isinstance(date_of_birth, str):
            raise InvalidTypeException(
                f"The date of birth provided is not a str (type provided is {type(name)})."
            )

        if date_of_birth == "":
            self._date_of_birth = "14-03-1879"  # Einstein birthdate
            return

        try:
            date_obj = datetime.datetime.strptime(date_of_birth, date_format)
        except ValueError:
            raise InvalidFormatException(f"Incorrect data format, should be DD-MM-YYYY (got {date_of_birth})")

        # TODO: check so the date is not in the future

        self._date_of_birth = date_of_birth

    @property
    def profile_picture(self) -> str:
        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, profile_picture: str):
        if not isinstance(profile_picture, str):
            raise InvalidTypeException(
                f"The link to profile picture provided is not a str (type provided is {type(profile_picture)})."
            )

        # TODO: add link validation from google cloud

        self._profile_picture = profile_picture

    @staticmethod
    def get_activation_token(expires_sec=1800):
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
    def verify_activation_token(token: str):
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
