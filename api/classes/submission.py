from __future__ import annotations
from datetime import time, datetime

from api import db
from bson import ObjectId

class Submission:
    date_submitted : time
    content : str
    filenames : list
    student_id : str
    assignment_id : str
    grade : int
    _id : str

    def __init__(
        self,
        date_submitted: time,
        content: str,
        filenames: list,
        student_id: str,
        assignment_id: str,
        grade: int = None,
        _id: str = None
    ):
        r"""Initializes the Submission object
        
        Parameters
        ----------
        date_submitted : datetime.datetime
            A utc time signature that specifies when this submission was submitted.
        content : str
            Content (as Quill deltas) of the submission.
        filenames : list
            Any associated files.
        grade : int, optional
            The grade received, defaults to None
        _id : str, optional
            Specifies the assignment _id, defaults to None
        """
        self.date_submitted = date_submitted
        self.content = content
        self.filenames = filenames
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.grade = grade
        self._id = _id if _id is not None else ''

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self.id = id

    def to_dict(self) -> dict:
        return {
            "date_submitted": str(self.date_submitted),
            "content": str(self.content),
            "filenames": self.filenames,
            "student_id": self.student_id,
            "assignment_id": self.assignment_id,
            "grade": self.grade,
            "id": self.id,
        }
    
    @classmethod
    def from_dict(cls, dictionary: dict) -> Submission:
        r"""Generates a Submission object from a dictionary.

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Submission parameters
        """

        return cls(**dictionary)

    @property
    def grade(self):
        return self._grade
        
    @grade.setter
    def grade(self, grade: int):
        self._grade = grade

    def update_grade(self, grade: int) -> bool:
        """Update the grade for this submission

        Parameters
        ----------
        grade : int
            The grade

        Returns
        -------
        bool
            `True` if operation was a success. `False` otherwise
        """
        try:
            self.grade = grade
            
            # TODO: Check that the grade is not bigger or smaller than the course range!!
            db.courses.find_one_and_update(
                {"assignments._id": self.assignment_id, "assignments.submissions._id": self.id},
                {"$set": {"assignments.$.submissions.$.grade": self.grade}}
            )

            return True
        except:
            logger.exception(
                f"Error while updating grade {grade} in submission {self.id}"
            )

            return False