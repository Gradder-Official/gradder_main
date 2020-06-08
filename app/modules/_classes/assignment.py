from datetime import time, datetime

from app import db


class Assignment:
    def __init__(self, date_assigned: time, assigned_by: int, assigned_to: str, due_by: datetime, subject: str, content: str, estimated_time: int, ID: str = None):
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

        self.ID = ID if ID is not None else Assignment.new_id(str(assigned_to))

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
        r"""Generates an Assignment object from a dictionary,

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Assignment parameters
        """
        return Assignment(**dictionary)

    @staticmethod
    def new_id(class_id: str):
        last_id_ref = db.collection_classes.document(
            class_id).collection('assignments').document('last_id')
        new_id = int(last_id_ref.get().to_dict()['last_id']) + 1

        last_id_ref.set({'last_id': new_id})

        return str(new_id)

    def add(self):
        try:
            db.collection_classes.document(self.assigned_to).collection("assignments").document(self.ID).set(self.to_dict())

            return True
        except BaseException as e:
            print(e)
            return False

    @staticmethod
    def get_by_class(class_id: str):
        class_obj = db.collection_classes.document(class_id).collection("assignments")

        class_obj = class_obj.stream()
        assignments = list()
        for assgn in class_obj:
            if not 'last_id' in assgn.to_dict():
                assignments.append(assgn.to_dict())

        return assignments
