from typing import List
import re

from . import Assignment

from app import db
from app.logs.user_logger import user_logger
from bson.objectid import ObjectId

class Classes:
    def __init__(self, department:str, number: int, name: str, teacher: str = None, students: List[str] = None, description: str = None, 
                       schedule_time: str = None, schedule_days: str = None, syllabus: str = None, assignments: List[Assignment] = None, ID: str = None,):
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
            'number': self.number,
            'name': self.name,
            'teacher': self.teacher,
            'students': self.students,
            'description': self.description,
            'schedule_time': self.schedule_time,
            'schedule_days': self.schedule_days,
            'syllabus': self.syllabus,
            'assignments': self.assignments
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
        return Classes(dictionary["department"], dictionary["number"], 
                        dictionary["name"], dictionary["teacher"], 
                        dictionary["students"], dictionary["description"], 
                        dictionary["schedule_time"], dictionary["schedule_days"], 
                        dictionary["syllabus"], 
                        list(map(lambda x: Assignment.from_dict(x), list(dictionary["assignments"]))) if "assignments" in dictionary else None,
                        ID=dictionary["_id"])

    def add(self):
        db.classes.insert_one(self.to_dict())
            # for assignment in self.assignments:
            #     self.add_assignment(assignment)
        # else:
        #     doc_ref = db.collection_classes.document()
        #     self.ID = doc_ref.id
        #     doc_ref.set(self.to_dict())

    @staticmethod
    def delete(ID: str):
        try:
            db.classes.remove({"_id": ID})
        except BaseException as e:
            user_logger.info(f"Error while deleting class {ID}: {e}")

    def get_assignments(self):
        assignments = list()
        for assignment in self.assignments:
            # Gets the dict object from the reference to the Firestore document stored in assignment,
            # creates an Assignment object from the dictionary and then appends it to the return object
            assignment.class_name = self.name

            assignments.append(assignment)
        
        return assignments

    def add_assignment(self, assignment: Assignment):
        try:
            dictionary = assignment.to_dict()
            dictionary["_id"] = ObjectId()
            db.classes.find_one_and_update({"_id": self.ID}, {"$push": {"assignments": dictionary}})
        except BaseException as e:
            user_logger.info(f"Error while adding assignment {assignment.ID}: {e}")

    def delete_assignment(self, assignment_id: str):
        try:
            db.classes.update({"_id": self.ID}, {"$pull": {'assignments': { "_id": assignment_id } } })
        except BaseException as e:
            user_logger.info(f"Error while deleting assignment {assignment_id} from class {self.ID}: {e}")

    @staticmethod
    def get_by_id(ID: str):
        return Classes.from_dict(db.classes.find_one({"_id": ObjectId(ID)}))

    def get_full_name(self) -> str:
        r'''Returns name in the format "SOС310 U.S. History"
        '''
        return self.department + str(self.number) + " " + self.name