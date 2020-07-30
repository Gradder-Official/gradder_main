from __future__ import annotations
from typing import Dict, List

from .user import User
from .course import Course


class Admin(User):
    _type = 'Admin'  # Immutable
    def ___init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        courses: List[str] = None,
        _id: str = None
    ):
        r"""Creates a user with Admin access

        This class is used for school admins that will have access to managing their school and teachers, 
        but with no access to grades or homework.

        Parameters
        ----------
        email: str
        first_name: str
        last_name: str
        courses: List[str]
            Holds the user's courses returned by the database
        _id: str, optional
            This user's ID, will be empty if not specified
        """
        super().__init__(email=email, first_name=first_name, last_name=last_name, _id=_id)
        self.courses = courses or []
    
    def __repr__(self) -> str:
        return f"<Admin { self.id }>"

    def to_dict(self) -> Dict:
        r"""
        Turns the admin class into a dictionary.
        """
        return super(User, self).to_dict()

    @staticmethod
    def from_dict(dictionary: dict) -> Admin:
        r""" Creates an Admin object from a dictionary.

        Parameters
        ----------
        dictionary: dict
        """
        return Admin(**dictionary)
    
    @staticmethod
    def get_by_id(id: str) -> Admin:
        r""" Returns the admin object based on id
        
        Parameters
        ----------
        id: str
            ObjectId in the string format. 
        """
        return Admin.from_dict(db.admins.find_one({"_id": ObjectId(id)}))

    @staticmethod
    def get_by_email(email: str) -> Admin:
        r"""Returns the admin object based on email
        
        Parameters
        ----------
        email: str
            String containing the email of the admin
        """
        return Admin.from_dict(db.admins.find_one({"email": email}))
    
    def get_course_names(self) -> Course:
        r"""Returns a list of the Teacher's courses

        Returns
        ------
        List[Tuple[str, str]]
            A list of a teacher's courses, represented as tuples (course-id, course-name).
        """
        courses = list()

        for course_id in db.courses.find():
            course_id = course_id.get("_id")
            courses.append((course_id, Course.get_by_id(course_id).name))

        return courses