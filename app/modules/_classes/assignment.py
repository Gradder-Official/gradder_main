from datetime import time, datetime
from typing import List
from app.logs.user_logger import user_logger
from app import db
from .submission import Submission


class Assignment:
    def __init__(self, title:str, date_assigned: time, assigned_by: int, assigned_to: str, due_by: datetime, content: str, filenames: list, 
                       estimated_time: int, submissions: List[Submission] = None, ID: str = None):
        r"""Initializes the Assignment object

        Parameters
        ----------
        title: str
            Title of the assignment
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
        ID : str, optional
            Specifies the assignment ID, generated automatically if not specified
        """
        self.title = title
        self.date_assigned = date_assigned
        self.assigned_by = assigned_by
        self.assigned_to = assigned_to
        self.due_by = due_by
        self.content = content
        self.filenames = filenames
        self.estimated_time = estimated_time
        self.submissions = submissions if submissions is not None else list()
        self.ID = ID

    def __repr__(self):
        return f'<Assignment { self.ID }>'

    def to_dict(self):
        return {
            'title': self.title,
            'date_assigned': str(self.date_assigned),
            'assigned_by': str(self.assigned_by),
            'assigned_to': str(self.assigned_to),
            'due_by': str(self.due_by),
            'content': str(self.content),
            'filenames': self.filenames,
            'estimated_time': str(self.estimated_time),
            'submissions': self.submissions
        }

    def to_json(self):
        return {
            'ID': str(self.ID),
            'title': self.title,
            'date_assigned': str(self.date_assigned),
            'assigned_by': str(self.assigned_by),
            'assigned_to': str(self.assigned_to),
            'due_by': str(self.due_by),
            'content': str(self.content),
            'filenames': self.filenames,
            'estimated_time': str(self.estimated_time),
            'submissions': list(map(lambda x: x.to_json(), self.submissions)),
            'class_name': self.class_name if self.class_name else ''
        }

    @staticmethod
    def from_dict(dictionary: dict):
        r"""Generates an Assignment object from a dictionary,

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Assignment parameters
        """
        return Assignment(dictionary["title"], dictionary["date_assigned"], dictionary["assigned_by"], 
                            dictionary["assigned_to"], dictionary["due_by"], 
                            dictionary["content"], dictionary["filenames"], 
                            dictionary["estimated_time"], 
                            list(map(lambda x: Submission.from_dict(x), dictionary["submissions"])) if dictionary['submissions'] is not None else None, 
                            ID=dictionary["_id"])
