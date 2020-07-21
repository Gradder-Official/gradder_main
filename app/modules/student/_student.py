from typing import List, Dict

from app import db
from app.modules._classes import Assignment, User, Classes, Submission
from bson import ObjectId
from typing import Dict, List
from flask_login import current_user


class Student(User):
    USERTYPE = "Student"

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: List[str] = None,
        assignments: List[str] = None,
        ID: str = None,
    ):
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
        self.assignments = assignments if assignments is not None else list()

    def __repr__(self):
        return f"<Student {self.ID}"

    def to_json(self) -> Dict[str, str]:
        """ Returns the user represented as a dict (equivalent to to_dict).
        """
        json_user = super().to_json()
        json_user["classes"] = self.classes
        json_user["assignments"] = self.assignments
        return json_user

    def to_dict(self) -> Dict[str, str]:
        """ Returns the user represented as a dict (equivalent to to_json).
        """
        return self.to_json()

    @staticmethod
    def from_dict(dictionary: dict):
        user = Student(
            email=dictionary["email"],
            first_name=dictionary["first_name"],
            last_name=dictionary["last_name"],
            ID=str(dictionary["_id"]) if "_id" in dictionary else None,
        )

        if "classes" in dictionary:
            user.classes.extend(dictionary["classes"])

        if "assignments" in dictionary:
            user.assignments.extend(dictionary["classes"])

        if "password" in dictionary:
            user.set_password(dictionary["password"])

        if "secret_question" in dictionary and "secret_answer" in dictionary:
            user.set_secret_question(
                dictionary["secret_question"], dictionary["secret_answer"]
            )

        return user

    @staticmethod
    def get_by_id(id: str):
        return Student.from_dict(super(Student, Student).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        return Student.from_dict(
            super(Student, Student).get_by_name("student", first_name, last_name)
        )

    @staticmethod
    def get_by_email(email: str):
        return Student.from_dict(super(Student, Student).get_by_email(email))

    def get_assignments(self) -> List[Assignment]:
        """ Gets a list of assignments from the database for this student.
        """
        assignments = list()
        for class_ref in self.classes:
            assignments.extend(Classes.get_by_id(class_ref).get_assignments())

        return assignments

    def add_submission(self, current_user_id, class_id, assignment_id, submission):
        dictionary = submission.to_dict()
        dictionary["student_id"] = self.ID
        dictionary["_id"] = ObjectId()
        db.classes.find_one_and_update(
            {"_id": ObjectId(class_id), "assignments._id": ObjectId(assignment_id)},
            {"$push": {"assignments.$.submissions": dictionary}},
        )
        unique_submission_string = (
            class_id + "_" + assignment_id + "_" + str(dictionary["_id"])
        )
        db.students.find_one_and_update(
            {"_id": ObjectId(current_user_id)},
            {"$push": {"assignments": unique_submission_string}},
        )
