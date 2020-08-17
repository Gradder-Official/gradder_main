from __future__ import annotations
from datetime import time, datetime

from api import db


class Submission:
    def __init__(
        self,
        date_submitted: time,
        content: str,
        filenames: list,
        student_id: str,
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
        self._grade = grade
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