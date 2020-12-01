from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional

from api import db
from api import root_logger as logger
from bson import ObjectId

from . import CalendarEvent
from . import Course
from . import SchoolConfig
from . import Student
from . import Teacher
from . import User


class Admin(User):
    _type = "Admin"  # Immutable

    def ___init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        courses: List[str] = None,
        _id: str = None,
        calendar: Optional[List[CalendarEvent]] = None,
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
        super().__init__(
            email=email,
            first_name=first_name,
            last_name=last_name,
            _id=_id,
            calendar=calendar,
            activated=True,
        )
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
        r"""Creates an Admin object from a dictionary.

        Parameters
        ----------
        dictionary: dict
        """
        if dictionary is None:
            return None

        try:
            return Admin(**dictionary)
        except Exception as e:
            logger.exception(
                f"Error while generating an Admin from dictionary {dictionary}"
            )
            return None

    def add(self) -> bool:
        r"""Adds the admin to the DB."""

        try:
            self.id = db.admins.insert_one(self.to_dict()).inserted_id
        except pymongo.errors.DuplicateKeyError:
            logger.exception(
                f"The Admin with the id {self.id} already exists, you should not be calling the add() method."
            )
            return False
        except Exception as e:
            logger.exception(f"Error while adding Admin {self.id}")
            return False
        else:
            return True

    def remove(self) -> bool:
        r"""Removes this admin from the database."""

        try:
            db.admins.delete_one({"_id": ObjectId(self.id)})
        except Exception as e:
            logger.exception(f"Error while removing Admin {self.id}")
            return False
        else:
            return True

    @staticmethod
    def get_by_id(id: str) -> Admin:
        r"""Returns the admin object based on id

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

    @staticmethod
    def get_courses() -> List[Course]:
        r"""Returns a list of the Admin's courses

        Returns
        ------
        List[Course]
            A list of an admin's courses, represented as tuples (course-id, course-name).
        """
        courses = list()

        for course_id in db.courses.find():
            course_id = course_id.get("_id")
            courses.append(Course.get_by_id(course_id))

        return courses

    @staticmethod
    def add_course(course: Course):
        r"""Adds a new course to the course collection

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
            logger.exception(f"Error while adding class {course.ID}")
            return False

    @staticmethod
    def add_student(class_id: str, email: str):
        r"""Adds a student to a course
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
        r"""Adds a teacher to a course
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
        r"""Returns Admin with a specified keyword.
        Parameters
        ---------
        first_name: str

        Returns
        ------
        List[Admin]
        """
        try:
            admins = db.admins.aggregate(
                [
                    {
                        "$search": {
                            "autocomplete": {"query": keyword, "path": "first_name"}
                        }
                    },
                    {"$project": {"_id": 1, "first_name": 1, "last_name": 1}},
                    {"$limit": 5},
                ]
            )

            possible_admins = []
            for admin in admins:
                possible_admins.append(Admin.from_dict(admin))
            return possible_admins

        except BaseException as e:
            logger.exception(f"Error while getting admin by name {id}: {e}")
            return None

    def get_course_names(self) -> List[(str, str)]:
        r"""Returns all course ids and names for a school in a list"""
        courses = list()

        for course in db.courses.find():
            course_id = course.get("_id")
            courses.append((course_id, Course.get_by_id(course_id).name))

        return courses

    def get_student_names(self) -> List[(str, str)]:
        r"""
        Returns a list of all ObjectId's and Names of Students
        """

        students = list()

        for student in db.students.find():
            student_id = student.get("_id")
            students.append((student_id, Student.get_by_id(student_id).name))

        return students

    def get_teacher_names(self) -> List[(str, str)]:
        r"""
        Returns all Teacher names, and ObjectId's of Students
        """

        teachers = list()

        for teacher in db.teachers.find():
            teacher_id = teacher.get("_id")
            teachers.append((teacher_id, Teacher.get_by_id(teacher_id).name))

        return teachers

    @staticmethod
    def add_student_to_parent(parent_id: str, student_id: str) -> bool:
        try:
            db.students.update_one(
                {"_id": ObjectId(student_id)},
                {"$push": {"parents": ObjectId(parent_id)}},
            )
            db.parents.update_one(
                {"_id": ObjectId(parent_id)},
                {"$push": {"children": ObjectId(student_id)}},
            )
            logger.debug(f"Added student {student_id} to parent {parent_id}")
            return True
        except:
            logger.error(f"Error adding student {student_id} to parent {parent_id}")
            return False

    @staticmethod
    def remove_student_from_parent(parent_id: str, student_id: str) -> bool:
        try:
            db.students.update_one(
                {"_id": ObjectId(student_id)},
                {"$pull": {"parents": ObjectId(parent_id)}},
            )
            db.parents.update_one(
                {"_id": ObjectId(parent_id)},
                {"$pull": {"children": ObjectId(student_id)}},
            )
            logger.debug(f"Removed student {student_id} from parent {parent_id}")
            return True
        except:
            logger.error(f"Error removing student {student_id} from parent {parent_id}")
            return False

        return teachers

    @staticmethod
    def update_school_settings(config: SchoolConfig):
        try:
            dictionary = config.to_dict()
            school_name = dictionary["school_name"]
            school_address = dictionary["school_address"]
            phone_number = dictionary["phone_number"]
            school_email = dictionary["school_email"]
            principal = dictionary["principal"]
            principal_email = dictionary["principal_email"]
            departments = dictionary["departments"]
            department_description = dictionary["deparment_description"]
            grade_weights = dictionary["grade_weights"]
            grading = dictionary["grading"]
            SchoolConfig.update(
                school_name,
                school_address,
                phone_number,
                school_email,
                principal,
                principal_email,
                departments,
                department_description,
                grade_weights,
                grading,
            )
            return True
        except:
            logger.exception(f"An error occured while updating school settings")
            return False
