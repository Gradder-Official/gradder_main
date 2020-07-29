from datetime import time, datetime
from typing import List

from api.classes import Submission

class Assignment:
    _id: str
    def __init__(
        self,
        title: str,
        date_assigned: time,
        assigned_by: int,
        assigned_to: str,
        due_by: datetime,
        content: str, #TODO: this should be represented int Deltas(JSON)
        filenames: list,
        estimated_time: int,
        submissions: List[Submission] = None,
        _id: str = None,
    ):
        r"""Initializes the Assignment object
        Parameters
        ----------
        title: str
            Title of the assignment
        date_assigned: datetime.datetime
            A UTC timestamp that specifies when this assignment was posted by a Teacher
        assigned_by: int
            Teacher ID that specifies who assigned this assignment
        assigned_to: int
            The class ID it was assigned to
        due_by: datetime.datetime
            A UTC timestamp that specifies when this assignment is due
        subject: str
            The subject of the assignment
        content: JSON object
            An JSON string that is the content of this assignment (may include links to the files on the server).
        estimated_time: int
            Estimated time in minutes that this assignment should take to complete (set by the teacher).
        _id: str, optional
            Specifies the assignment ID, will be empty if not specified
        """
        if _id is not None:
            self.id = _id

    def __repr__(self):
        return f"<Assignment { self.id }>"
        
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter 
    def id(self, id: str):
        self._id = id

