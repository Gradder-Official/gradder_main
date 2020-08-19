from __future__ import annotations
from typing import Dict, List
from bson import ObjectId

from api import db
from api import root_logger as logger

from .user import User
from .course import Course

class Admin(User):
    _type = 'Admin'  # Immutable
    def ___init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        courses: List[str] = None,
        _id: str = None
    ):
        r"""Creates a user with Admin access

        This class is used for school admins that will have access to managing their school and teachers, 
        but with no access to grades or homework.

        Parameters
        ----------
        email: str
        first_name: str
        last_name: str
        courses: List[str]
            Holds the user's courses returned by the database
        _id: str, optional
            This user's ID, will be empty if not specified
        """
        super().__init__(email=email, first_name=first_name, last_name=last_name, _id=_id)
        self.courses = courses or []
    
    def __repr__(self) -> str:
        return f"<Admin { self.id }>"

    def to_dict(self) -> Dict:
        r"""
        Turns the admin class into a dictionary.
        """
        return super().to_dict()

    @staticmethod
    def from_dict(dictionary: dict) -> Admin:
        r""" Creates an Admin object from a dictionary.

        Parameters
        ----------
        dictionary: dict
        """
        if dictionary is None:
            return None
            
        try:
            return Admin(**dictionary)
        except Exception as e:
            logger.exception(f"Error while generating an Admin from dictionary {dictionary}: {e}")
            return None
    
    def add(self) -> bool:
        r"""Adds the admin to the DB.
        """

        try:
            self.id = db.admins.insert_one(self.to_dict()).inserted_id
        except Exception as e:
            logger.exception(f"Error while adding Admin {self.id}: {e}")
            return False
        else:
            return True

    def remove(self) -> bool:
        r"""Removes this admin from the database.
        """

        try:
            db.admins.delete_one({'_id': ObjectId(self.id)})
        except Exception as e:
            logger.exception(f"Error while removing Admin {self.id}: {e}")
            return False
        else:
            return True
    
    @staticmethod
    def get_by_id(id: str) -> Admin:
        r""" Returns the admin object based on id
        
        Parameters
        ----------
        id: str
            ObjectId in the string format. 
        """
        return Admin.from_dict(db.admins.find_one({"_id": ObjectId(id)}))

    @staticmethod
    def get_by_email(email: str) -> Admin:
        r"""Returns the admin object based on email
        
        Parameters
        ----------
        email: str
            String containing the email of the admin
        """
        return Admin.from_dict(db.admins.find_one({"email": email}))
    
    def get_course_names(self) -> Course:
        r"""Returns a list of the Teacher's courses

        Returns
        ------
        List[Tuple[str, str]]
            A list of a teacher's courses, represented as tuples (course-id, course-name).
        """
        courses = list()

        for course_id in db.courses.find():
            course_id = course_id.get("_id")
            courses.append((course_id, Course.get_by_id(course_id).name))

        return courses

    @staticmethod
    def add_course(course: Course):
        r""" Adds a new course to the course collection

        Adds a course to the course collection with empty students, assignments, and syllabus lists
        
        Parameters
        ----------
        courses : Course
            Course object
        """
        try:
            dictionary = course.to_dict()
            dictionary["_id"] = ObjectId()
            dictionary["students"] = list()
            dictionary["assignments"] = list()
            dictionary["syllabus"] = list()
            db.courses.insert_one(dictionary)
            return True
        except BaseException as e:
            root_logger.exception(f"Error while adding class {course.ID}: {e}")
            return False

    @staticmethod
    def add_student(class_id: str, email: str):
        r""" Adds a student to a course
        Gets a student from their email and adds the student's _id to the specific course's student ids' field
        
        Parameters
        ----------
        class_id : str
            The ObjectId of the specific course in string format.
        email: str
            The email of the student
        """
        student = Student.get_by_email(email)
        db.courses.update_one(
            {"_id": ObjectId(class_id)}, {"$push": {"students": ObjectId(student.ID)}}
        )

    @staticmethod
    def add_teacher(class_id: str, email: str):
        r""" Adds a teacher to a course
        Gets a teacher from their email and adds the teacher's _id to the specific course's teacher id field
        
        Parameters
        ----------
        class_id : str
            The ObjectId of the specific course.
        email: str
            The email of the teacher
        """
        teacher = Teacher.get_by_email(email)
        db.courses.update_one(
            {"_id": ObjectId(class_id)}, {"$set": {"teacher": ObjectId(teacher.ID)}}
        )

    @staticmethod
    def get_by_keyword(keyword: str) -> Admin:
        r""" Returns Admin with a specified keyword.
        Parameters
        ---------
        first_name: str

        Returns
        ------
        List[Admin]
        """
        try:
            admins = db.admins.find({"first_name": {"$regex": ".*" + keyword + ".*"}})

            possible_admins = []
            for admin in admins:
                possible_admins.append(Admin.from_dict(admin))
            return possible_admins

        except BaseException as e:
            logger.exception(f"Error while getting admin by name {id}: {e}")
            return None
            
    def get_course_names(self) -> List[(str, str)]:
        r""" Returns all course ids and names for a school in a list
        """
        courses = list()

        for course in db.courses.find():
            course_id = course.get("_id")
            courses.append((course_id, Course.get_by_id(course_id).name))

        return courses
