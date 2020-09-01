from __future__ import annotations
from typing import Dict, List, Tuple, Union, Optional
from bson import ObjectId

from api import db
from api import root_logger as logger
from . import User, CalendarEvent

class Teacher(User):
    _type = 'Teacher'  # Immutable

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        password: Optional[Union[bytes, str]] = None,
        courses: Optional[list] = None,
        _id: Optional[Union[ObjectId, str]] = None,
        activated: Optional[bool] = False,
        calendar: Optional[List[CalendarEvent]] = None
    ):

        r""" Initializes a user of Teacher type.

        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        classes : list
        _id : str
        activated : bool
            The activation status of the user, by default False
        """
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, _id=_id, password=password, calendar=calendar
        )
        self.courses = courses or []

    def __repr__(self):
        return f"<Teacher {self.id}>"

    def to_dict(self) -> Dict[str, str]:
        r"""A representation of the object in a dictionary format.
        """
        dict_user = super().to_dict()
        dict_user["courses"] = self.courses
        dict_user["activated"] = self.activated
        return dict_user

    @staticmethod
    def from_dict(dictionary: dict) -> Teacher:
        r"""Creates a Teacher from a dictionary.

        Parameters
        ---------
        dictionary : dict

        Returns
        -------
        Teacher
        """
        if dictionary is None:
            return None
            
        try:
            return Teacher(**dictionary)
        except Exception as e:
            logger.exception(f"Error while generating a Teacher from dictionary {dictionary}")
            return None

    def add(self) -> bool:
        r"""Adds the teacher to the DB.
        """

        try:
            self.id = db.teachers.insert_one(self.to_dict()).inserted_id
        except pymongo.errors.DuplicateKeyError:
            logger.exception(f"The Teacher with the id {self.id} already exists, you should not be calling the add() method.")
            return False
        except Exception as e:
            logger.exception(f"Error while adding Teacher {self.id}")
            return False
        else:
            return True

    def remove(self) -> bool:
        r"""Removes this teacher from the database.
        """

        try:
            db.teachers.delete_one({'_id': ObjectId(self.id)})
        except Exception as e:
            logger.exception(f"Error while removing Teacher {self.id}")
            return False
        else:
            return True

    @staticmethod
    def get_by_id(id: str) -> Teacher:
        r"""Returns a Teacher object with a specified id.

        Parameters
        ---------
        id : str
            ID to look up in the database

        Returns
        -------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"_id": ObjectId(id)}))
        except:
            logger.info(f"Error when returning Teacher by id {id}")

    @staticmethod
    def get_by_email(email: str) -> Teacher:
        r""" Returns Teacher with a specified email.
        
        Parameters
        ---------
        email : str

        Returns
        ------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"email": email}))
        except:
            logger.info(f"Error when returning Teacher by email {email}")

    def get_course_names(self) -> List[Tuple[str, str]]:
        r"""Returns a list of the Teacher's courses

        Returns
        ------
        List[Tuple[str, str]]
            A list of a teacher's courses, represented as tuples (course-id, course-name).
        """
        from api.classes import (
            Course,
        )  # If put at top, creates a circular import problem

        courses = list()
        for course_id in self.courses:
            courses.append((course_id, Course.get_by_id(course_id).name))

        return courses

    def activate(self):
        r"""Activates the user

        Returns
        ------
        True if operation was successful, false if it was not
        """
        try:
            db.teachers.update({"_id": ObjectId(self._id)}, {"$set": {"activated": True}})
            self.activated = True
            return True
        except:
            return False

    def set_password(self, password:str):
        r"""Sets the password after the user activates their account

        Parameters
        ---------
        password : str

        Returns
        ------
        True if operation was successful, false if it was not
        """
        try:
            self.password = password
            db.teachers.update({"_id": self.id}, {"$set": {"password": self.password}})
            return True
        except:
            return False