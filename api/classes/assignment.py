from datetime import time, datetime
from typing import List

class Assignment:
    def __init__(
        self,
        title: str,
        date_assigned: time,
        assigned_by: int,
        assigned_to: str,
        due_by: datetime,
        content: str,
        filenames: list,
        estimated_time: int,
        submissions: List[Submission] = None,
        ID: str = None,
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
            An HTML string that is the content of this assignment (may include links to the files on the server).
        estimated_time: int
            Estimated time in minutes that this assignment should take to complete (set by the teacher).
        ID: str, optional
            Specifies the assignment ID, generated automatically if not specified
        """
    pass
