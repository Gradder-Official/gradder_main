from datetime import time, datetime
from . import Teacher, Student
from typing import List

# Defines a Class type as a list of Students enrolled in a class
Class = List[Student]


class Assignment:
    def __init__(self, date_assigned: time, assigned_by: int, assigned_to: int, due_by: datetime, subject: str, content: str, estimated_time: int, ID: str = None):
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
        self.subject = subject
        self.content = content
        self.estimated_time = estimated_time

        from app import db
        # TODO: rewrite this piece for a better ID generation
        self.ID = ID if ID is not None else db.get_new_assignment_id()

    def to_dict(self):
        return {
            'date_assigned': str(self.date_assigned),
            'assigned_by': str(self.assigned_by),
            'assigned_to': str(self.assigned_to),
            'due_by': str(self.due_by),
            'subject': str(self.subject),
            'content': str(self.content),
            'estimated_time': str(self.estimated_time),
            'ID': str(self.ID)
        }

    @staticmethod
    def from_dict(dictionary: dict):
        r"""Generates a Student object from a dictionary,

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Student parameters
        """
        return Student(**dictionary)
