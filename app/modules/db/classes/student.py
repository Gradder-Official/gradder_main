from .user import User
from .access_level import ACCESS_LEVEL
from typing import Dict, List

# A type that defines a dictionary of grades: subjects are keys and lists of integer grades are values
# TODO: add handling for non-integer grading systems later
gradeDict = Dict[str, List[int]]


class Student(User):
    def __init__(self, email: str, first_name: str, last_name: str, class_names: List[int] = None, ID: str = None, grades: gradeDict = None):
        r"""Initializes a Student object.

        Parameters
        ----------
        email : str
            Student's email address.
        first_name : str
            Student's first name as it was entered in the signup form or by an admin.
        last_name : str
            Student's last name as it was entered in the singup form or by an admin.
        class_names : List[int], optional
            A list of integer numbers that correspond to the IDs of the classes a student belongs in. Defaults to None, but must be set later.
        ID : str, optional
            User's string ID. If not specified, defaults to None and then iss auto-generated.
        grades : gradeDict, optional
            User's grades formatted as a dictionary with subject's name as keys and lists of integer grades as values.
        """
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
        """ Returns the user represented as a dict (equivalent to to_dict).
        """
        json_user = super().to_json()

        json_user['class_names'] = self.class_names
        json_user['grades'] = self.grades

        return json_user

    def to_dict(self):
        """ Returns the user represented as a dict (equivalent to to_json).
        """
        return self.to_json()

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
        """ Gets a list of assignments from the database for this student.
        """
        from app import db
        assignments = list()
        for class_ref in self.class_names:
            assignments.extend(db.get_assignments_by_class(str(class_ref)))

        return assignments
