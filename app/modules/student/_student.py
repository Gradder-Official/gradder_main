from __future__ import annotations

from app import db
from app.modules._classes import Assignment, User, Classes


from typing import List, Dict

class Student(User):
    USERTYPE = 'Student'

    def __init__(self, email: str, first_name: str, last_name: str, classes: List[str] = None, ID: str = None):
        r"""Initializes a Student object.

        Parameters
        ----------
        email : str
            Student's email address.
        first_name : str
            Student's first name as it was entered in the sign-up form or by an admin.
        last_name : str
            Student's last name as it was entered in the sign-up form or by an admin.
        classes : List[str], optional
            A list of string values that correspond to the IDs of the classes a student belongs in. Defaults to None, but must be set later.
        ID : str, optional
            User's string ID. If not specified, defaults to None and then iss auto-generated.
        """
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        
        self.classes = classes if classes is not None else list()

    def __repr__(self):
        return f'<Student {self.ID}'

    def to_json(self) -> Dict[str, str]:
        """ Returns the user represented as a dict (equivalent to to_dict).
        """
        json_user = super().to_json()
        json_user['classes'] = self.classes

        return json_user

    def to_dict(self) -> Dict[str, str]:
        """ Returns the user represented as a dict (equivalent to to_json).
        """
        return self.to_json()

    @staticmethod
    def from_dict(dictionary: dict) -> Student:
        user = Student(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'classes' in dictionary:
            user.classes.extend(dictionary['classes'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user

    @staticmethod
    def get_by_id(id: str) -> Student:
        return Student.from_dict(super(Student, Student).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str) -> Student:
        return Student.from_dict(super(Student, Student).get_by_name("student", first_name, last_name))

    @staticmethod
    def get_by_email(email: str) -> Student:
        return Student.from_dict(super(Student, Student).get_by_email(email))

    def get_assignments(self) -> List[Assignment]:
        """ Gets a list of assignments from the database for this student.
        """
        assignments = list()
        for class_ref in self.classes:
            assignments.extend(Classes.get_by_id(class_ref).get_assignments())

        return assignments
