from typing import List
import re

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
        dict_object = {
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
        
        return dict_object
    
    def to_json(self):
        from app.modules.student._student import Student
        # JSON object to be passed on to HTML templates
        # 'admin_info' should only be read-only for everyone except admins, 
        # teacher_info should only be read-only for everyone except teachers
        json_object = {
            'admin_info': {
                'department': self.department,
                'number': str(self.number),
                'name': self.name,
                'teacher': self.teacher,
                'schedule_time': self.schedule_time,
                'schedule_days': self.schedule_days,
            },
            'teacher_info': {
                'description': self.description,
                'syllabus': self.syllabus,
            },
            'immutable_info': {
                'alias': self.department + "_" + str(self.number) + "_" + re.sub(r'[^a-zA-Z]+', '', self.name.lower()),
                'full_name': self.get_full_name(),
                'ID': self.ID,
            },
            'students': 
                [Student.get_by_id(student_id).to_dict() for student_id in self.students],
        }

        return json_object

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

    def get_assignments(self):
        assignments = list()
        for assignment in db.collection_classes.document(self.ID).collection('assignments').stream():
            # Gets the dict object from the reference to the Firestore document stored in assignment,
            # creates an Assignment object from the dictionary and then appends it to the return object
            temp_assignment = Assignment.from_dict(assignment.to_dict())
            temp_assignment.class_name = self.name

            assignments.append(temp_assignment)
        
        return assignments

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

    def get_full_name(self) -> str:
        r'''Returns name in the format "SOС310 U.S. History"
        '''
        return self.department + str(self.number) + " " + self.name