from datetime import datetime
from . import Teacher, Student
from typing import List

Class = List[Student]

class Assignment:
    def __init__(self, date_assigned:datetime, assigned_by:Teacher, assigned_to:Class, due_by:datetime, content: str, estimated_time:int, ID:str=None):
        r"""Initializes the Assignment object

        Parameters
        ----------
        date_assigned: datetime.datetime
            A utc time signature that specifies when this assignment was posted by a Teacher.
        assigned_by: Teacher
            Teacher object that specifies who assigned this assignment.
        assigned_to: Class=List[Student]
            An object of type Class, equivalent to List[Student], which contains Students that this assignment is assigned to.
        due_by: datetime.datetime
            A utc time signature that specifies when this assignment is due.
        content: HTML string
            An HTML string that is the content of this assignment (may include links to the files on the server).
        estimated_time: int
            Estimated time in minutes that this assignment should take to complete (set by the teacher).
        ID: str, optional
            Specifies the assignment ID, generated automatically if not specified
        """
        self.date_assigned = date_assigned
        self.assigned_by = assigned_by
        self.assigned_to = assigned_to
        self.due_by = due_by
        self.content = content
        self.estimated_time = estimated_time



