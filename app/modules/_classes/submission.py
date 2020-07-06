from datetime import time, datetime
from app.logs.user_logger import user_logger
from app import db


class Submission:
    def __init__(self, date_submitted: time, content: str, file_links: list, ID: str = None):
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
        self.date_submitted = date_submitted
        self.content = content
        self.file_links = file_links
        self.ID = ID

    def to_dict(self):
        return {
            'date_submitted': str(self.date_submitted),
            'comment': str(self.content),
            'file_links': self.file_links,
        }

    def to_json(self):
        return {
            'date_submitted': str(self.date_submitted),
            'comment': str(self.content),
            'file_links': self.file_links,
        }

    @staticmethod
    def from_dict(dictionary: dict):
        r"""Generates an Assignment object from a dictionary,

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Assignment parameters
        """
        return Submission(dictionary["date_submitted"], 
                          dictionary["comment"], dictionary["file_links"], ID=dictionary["_id"])
