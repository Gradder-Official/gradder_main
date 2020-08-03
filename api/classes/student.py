from __future__ import annotations
from typing import Dict, List, Tuple
from bson import ObjectId

from api import db
from api import root_logger as logger

from .submission import Submission
from .user import User
from . import Assignment, Course

class Student(User):
    _type = 'Student'  # Immutable

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: List[str] = None,
        assignments: List[str] = None,
        _id: str = None
    ):
        """Initialises a user of Student type

        Parameters
        ----------
        email : str
            The user's email
        first_name : str
            The user's first name
        last_name : str
            The user's last name
        classes : List[str], optional
            The classes the user is part of, by default None
        assignments : List[str], optional
            The assignments the user has, by default None
        _id : str, optional
            The ID of the user, by default None
        """
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, _id=_id
        )

        self.classes = classes or []
        self.assignments = assignments or []
    
    def __repr__(self):
        return f"<Student {self.id}>"
    
    def to_dict(self) -> Dict[str, str]:
        """A dictionary representation of the Student

        Returns
        -------
        Dict[str, str]
            The dictionary
        """
        return {
            **super().to_dict(),
            'classes': self.classes,
            'assignments': self.assignments
        }
    
    @staticmethod
    def get_by_id(id: str) -> Student:
        r"""Returns a Student object with a specified id.

        Parameters
        ---------
        id: str
            ID to look up in the database

        Returns
        -------
        Student
        """
        try:
            return Student.from_dict(db.students.find_one({"_id": ObjectId(id)}))
        except BaseException as e:
            # TODO: add logger
            return None

    @staticmethod
    def get_by_email(email: str) -> Student:
        r""" Returns Student with a specified email.
        Parameters
        ---------
        email: str

        Returns
        ------
        Student
        """
        try:
            return Student.from_dict(db.students.find_one({"email": email}))
        except BaseException as e:
            # TODO: add logger
            return None

    @staticmethod
    def from_dict(dictionary: dict) -> Student:
        r"""Creates a Student from a dictionary.

        Parameters
        ---------
        dictionary: dict

        Returns
        -------
        Student
        """
        return Student(**dictionary)

    def add(self) -> bool:
        r"""Adds the student to the DB.
        """

        try:
            self.id = db.students.insert_one(self.to_dict()).inserted_id
        except Exception as e:
            logger.exception(f"Error while adding Student {self.id}: {e}")
            return False
        else:
            return True

    def get_assignments(self) -> List[Assignment]:
        """Gets a list of assignments from the database for this student
        """
        assignments = list()
        for class_ref in self.classes:
            assignments.extend(Course.get_by_id(class_ref).get_assignments())

        return assignments

    def add_submission(
        self,
        class_id: str,
        assignment_id: str,
        submission: Submission
    ):
        """Add a submission as this student

        Parameters
        ----------
        class_id : str
            The ID of the class this submission is for
        assignment_id : str
            The ID of the assignment this submission is for
        submission : Submission
            The submission
        """
        dictionary = submission.to_dict()
        dictionary["student_id"] = self._id
        dictionary["_id"] = ObjectId()
        db.courses.find_one_and_update(
            {"_id": ObjectId(class_id), "assignments._id": ObjectId(assignment_id)},
            {"$push": {"assignments.$.submissions": dictionary}},
        )
        unique_submission_string = (
            class_id + "_" + assignment_id + "_" + str(dictionary["_id"])
        )
        db.students.find_one_and_update(
            {"_id": ObjectId(self._id)},
            {"$push": {"assignments": unique_submission_string}},
        )
