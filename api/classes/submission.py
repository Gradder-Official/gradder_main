from __future__ import annotations
from datetime import time, datetime

from api import db


class Submission:
    def __init__(
        self, date_submitted: time, content: str, filenames: list, _id: str = None
    ):
        r"""Initializes the Assignment object
        Parameters
        ----------
        date_assigned : datetime.datetime
            A utc time signature that specifies when this assignment was posted by a Teacher.
        assigned_by : int
            Teacher id that specifies who assigned this assignment.
        assigned_to : int
            A class ID it was assigned to. 
        due_by : datetime.datetime
            A utc time signature that specifies when this assignment is due.
        subject : str
            The subject.
        content : HTML string
            An HTML string that is the content of this assignment (may include links to the files on the server).
        estimated_time : int
            Estimated time in minutes that this assignment should take to complete (set by the teacher).
        _id : str, optional
            Specifies the assignment _id, defaults to None
        """
        self.date_submitted = date_submitted
        self.content = content
        self.filenames = filenames
        self._id = _id if _id is not None else ''

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, _id: str):
        self.id = _id

    def to_dict(self) -> dict:
        return {
            "date_submitted": str(self.date_submitted),
            "content": str(self.content),
            "filenames": self.filenames,
        }
    
    @staticmethod
    def from_dict(dictionary: dict) -> Submission:
        r"""Generates a Submission object from a dictionary.

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Submission parameters
        """

        return Submission(**dictionary)