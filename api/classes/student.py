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
        password: str = None,
        courses: List[str] = None,
        assignments: List[str] = None,
        _id: str = None
    ):
        """Initialises a user of Student type

        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        password : str
        courses : List[str], optional
            The courses the student is in, by default None
        assignments : List[str], optional
            The assignments the user has, by default None
        _id : str, optional
            The ID of the user, by default None
        """
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, _id=_id, password=password
        )

        self.courses = courses or []
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
            'courses': self.courses,
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
            logger.exception(f"Error while getting a student by id {id}: {e}")
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

    def remove(self) -> bool:
        r"""Removes this student from the database.
        """

        try:
            db.students.delete_one({'_id': self.id})
        except Exception as e:
            logger.exception(f"Error while removing Student {self.id}: {e}")
            return False
        else:
            return True

    def get_assignments(self) -> List[Assignment]:
        """Gets a list of assignments from the database for this student
        """
        assignments = list()
        for course_id in self.courses:
            assignments.extend(Course.get_by_id(course_id).get_assignments())

        #TODO: add logger

        return assignments

    def add_submission(
        self,
        course_id: str,
        assignment_id: str,
        submission: Submission
    ):
        """Add a submission as this student

        Parameters
        ----------
        course_id : str
            The ID of the course this submission is for
        assignment_id : str
            The ID of the assignment this submission is for
        submission : Submission
            The submission
        """
        submission.id = str(ObjectId())

        dictionary = {
            **submission.to_dict(),
            "student_id" : self.id,
        }

        db.courses.find_one_and_update(
            {"_id": ObjectId(course_id), "assignments._id": ObjectId(assignment_id)},
            {"$push": {"assignments.$.submissions": dictionary}},
        )

        #TODO: add logger

        unique_submission_string = course_id + "_" + assignment_id + "_" + submission.id

        db.students.find_one_and_update(
            {"_id": ObjectId(self.id)},
            {"$push": {"assignments": unique_submission_string}},
        )

        #TODO: add logger
