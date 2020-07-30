from __future__ import annotations
from typing import Dict, List, Tuple
from bson import ObjectId

from api.classes import User
from api import db


class Teacher(User):
    _type = Teacher  # Immutable

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: list = None,
        _id: str = None,
    ):

        r""" Initializes a user of Teacher type.

        Parameters
        ----------
        email: str
        first_name: str
        last_name: str
        classes: list
        _id: str
        """
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, id=_id
        )
        self.classes = classes or []

    def __repr__(self):
        return f"<Teacher {self.id}>"

    def to_dict(self) -> Dict[str, str]:
        r"""A representation of the object in a dictionary format.
        """
        dict_user = super(User, self).to_dict()
        dict_user["classes"] = self.classes

        return dict_user

    @staticmethod
    def get_by_id(id: str) -> Teacher:
        r"""Returns a Teacher object with a specified id.

        Parameters
        ---------
        id: str
            ID to look up in the database

        Returns
        -------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"_id": ObjectId(id)}))
        except BaseException as e:
            # TODO: add logger
            return None

    @staticmethod
    def get_by_email(email: str) -> Teacher:
        r""" Returns Teacher with a specified email.
        Parameters
        ---------
        email: str

        Returns
        ------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"email": email}))
        except BaseException as e:
            # TODO: add logger
            return None

    @staticmethod
    def from_dict(dictionary: dict) -> Teacher:
        r"""Creates a Teacher from a dictionary.

        Parameters
        ---------
        dictionary: dict

        Returns
        -------
        Teacher
        """
        return Teacher(**dictionary)

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
