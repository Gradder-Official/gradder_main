from __future__ import annotations

from datetime import datetime
from datetime import time
from typing import List

from api.tools.exceptions import InvalidFormatException
from api.tools.exceptions import InvalidTypeException
from bson import ObjectId

from .submission import Submission


class Assignment:
    _id: str

    def __init__(
            self,
            title: str,
            date_assigned: time,
            assigned_by: int,
            assigned_to: str,
            due_by: datetime,
            content: str,  # TODO: this should be represented int Deltas(JSON)
            filenames: list,
            estimated_time: int,
            # weight: int,
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
        self.title = title
        self.date_assigned = date_assigned
        self.assigned_by = assigned_by
        self.assigned_to = assigned_to
        self.due_by = due_by
        self.content = content
        self.filenames = filenames
        self.estimated_time = estimated_time
        self.submissions = submissions or []
        # self.weight = weight

        if _id is not None:
            self.id = _id

    def __repr__(self):
        return f"<Assignment { self.id }>"

    def to_dict(self):
        return {
            "title": self.title,
            "date_assigned": self.date_assigned,
            "assigned_by": self.assigned_by,
            "assigned_to": self.assigned_to,
            "due_by": self.due_by,
            "content": self.content,
            "filenames": self.filenames,
            "estimated_time": self.estimated_time,
            "submissions": self.submissions,
            "id": self.id,
        }

    @classmethod
    def from_dict(cls, assignment: dict) -> object:
        return cls(**assignment)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        if id is not str:
            raise InvalidTypeException(
                f"The id provided is not a str (type provided is {type(id)}).")

        try:
            ObjectId(id)
        except Exception as e:
            raise InvalidFormatException(
                f"Cannot convert provided id to bson.ObjectId")

        self._id = id
