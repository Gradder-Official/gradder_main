from .user import User
from .access_level import ACCESS_LEVEL
from typing import Dict, List

gradeDict = Dict[str, List[int]]


class Student(User):
    def __init__(self, email: str, first_name: str, last_name: str, class_names: List[int] = None, ID: str = None, grades: gradeDict = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='student', ID=ID)
        if class_names is not None:
            self.class_names = class_names
        else:
            self.class_names = list()

        self.access_level = ACCESS_LEVEL.STUDENT

        if grades is not None:
            self.grades = grades
        else:
            self.grades = dict()

    def __repr__(self):
        return f'<Student {self.ID}'

    def to_json(self):
        json_user = super().to_json()

        json_user['class_names'] = self.class_names
        json_user['grades'] = self.grades

        return json_user

    @staticmethod
    def from_dict(dictionary: dict):
        user = Student(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'class_names' in dictionary:
            user.class_names.extend(dictionary['class_names'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        if 'grades' in dictionary:
            user.add_grades(dictionary['grades'])

        return user

    def add_grades(self, new_grades: gradeDict):
        self.grades.update(new_grades)

    def get_assignments(self):
        from app import db
        assignments = list()
        for class_ref in self.class_names:
            assignments.extend(db.get_assignments_by_class(str(class_ref)))

        return assignments
