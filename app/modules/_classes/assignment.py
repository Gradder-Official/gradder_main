from datetime import time, datetime
from app.logs.user_logger import user_logger
from app import db


class Assignment:
    def __init__(self, date_assigned: time, assigned_by: int, assigned_to: str, due_by: datetime, content: str, file_links: list, 
                       estimated_time: int, ID: str = None):
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
        ID : str, optional
            Specifies the assignment ID, generated automatically if not specified
        """
        self.date_assigned = date_assigned
        self.assigned_by = assigned_by
        self.assigned_to = assigned_to
        self.due_by = due_by
        self.content = content
        self.file_links = file_links
        self.estimated_time = estimated_time
        self.ID = ID

    def to_dict(self):
        return {
            'date_assigned': str(self.date_assigned),
            'assigned_by': str(self.assigned_by),
            'assigned_to': str(self.assigned_to),
            'due_by': str(self.due_by),
            'content': str(self.content),
            'file_links': self.file_links,
            'estimated_time': str(self.estimated_time),
            'ID': str(self.ID)
        }

    @staticmethod
    def from_dict(dictionary: dict):
        r"""Generates an Assignment object from a dictionary,

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Assignment parameters
        """
        return Assignment(**dictionary)
