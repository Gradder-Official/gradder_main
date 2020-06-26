from typing import List
from . import Assignment

from app import db
from app.logs.user_logger import user_logger

class Classes:
    def __init__(self, department:str, number: int, name: str, ID: str = None, teacher: str = None, students: List[str] = None, description: str = None, 
                       schedule_time: str = None, schedule_days: str = None, syllabus: str = None, assignments: List[Assignment] = None):
        self.department = department
        self.number = number
        self.name = name
        self.ID = ID
        self.teacher = teacher
        self.students = students
        self.description = description
        self.schedule_time = schedule_time
        self.schedule_days = schedule_days
        self.syllabus = syllabus
        self.assignments = assignments
    
    def __repr__(self):
        return f'<Class {self.ID}>'
    
    def to_dict(self):
        return {
            'department': self.department,
            'number': str(self.number),
            'name': self.name,
            'ID': self.ID,
            'teacher': self.teacher,
            'students': self.students,
            'description': self.description,
            'schedule_time': self.schedule_time,
            'schedule_days': self.schedule_days,
            'syllabus': self.syllabus
        }
    
    def to_json(self):
        return self.to_dict()

    @staticmethod
    def from_dict(dictionary: dict):
        return Classes(**dictionary)

    def add(self):
        if self.ID is not None:
            db.collection_classes.document(self.ID).set(self.to_dict())
            for assignment in self.assignments:
                self.add_assignment(assignment)
        else:
            doc_ref = db.collection_classes.document()
            self.ID = doc_ref.id
            doc_ref.set(self.to_dict())

    @staticmethod
    def delete(ID: str):
        try:
            db.collection_classes.document(ID).delete()
        except BaseException as e:
            user_logger.info(f"Error while deleting class {ID}: {e}")
    
    def add_assignment(self, assignment: Assignment):
        try:
            doc_ref = db.collection_classes.document(self.ID).collection('assignments').document()
            assignment.ID = doc_ref.id
            doc_ref.set(assignment.to_dict())
        except BaseException as e:
            user_logger.info(f"Error while adding assignment {assignment.ID}: {e}")

    def delete_assignment(self, assignment_id: str):
        try:
            db.collection_classes.document(self.ID).collection('assignments').document(assignment_id).delete()
        except BaseException as e:
            user_logger.info(f"Error while deleting assignment {assignment_id} from class {self.ID}: {e}")

    @staticmethod
    def get_by_id(ID: str):
        return Classes.from_dict(db.collection_classes.document(ID).get().to_dict())