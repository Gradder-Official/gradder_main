from __future__ import annotations
from typing import Dict, List, Tuple
from bson import ObjectId

from api import db, root_logger as logger

from .assignment import Assignment


class Course:
    _id : str
    def __init__(
        self,
        department: str,
        number: int,
        name: str,
        teacher: str = None,
        students: List[str] = None,
        description: str = "Description",
        schedule_time: str = None,
        schedule_days: str = None,
        syllabus: Tuple[str, str] = None,
        assignments: List[Assignment] = None,
        _id: str = None,
    ):
        """Initialises the Course object

        Parameters
        ----------
        department : str
            The department this course is under
        number : int
            The course number
        name : str
            The name of the course
        teacher : str, optional
            The teacher giving the course, by default None
        students : List[str], optional
            The students in the course, by default None
        description : str, optional
            The description of the course, by default "Description"
        schedule_time : str, optional
            The scheduled time for the course, by default None
        schedule_days : str, optional
            The scheduled days for the course, by default None
        syllabus : Tuple[str, str], optional
            The syllabus for this course, by default None
        assignments : List[Assignment], optional
            The assignments under this course, by default None
        _id : str, optional
            The ID of the course, by default None
        """
        self.department = department
        self.number = number
        self.name = name
        self.teacher = teacher
        self.students = students or []
        self.description = description
        self.schedule_time = schedule_time
        self.schedule_days = schedule_days
        self.syllabus = syllabus
        self.assignments = assignments or []
        if _id is not None:
            self.id = _id

    def __repr__(self):
        return f"<Course {self.id}>"

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    def to_dict(self) -> Dict[str, str]:
        dict_course = {
            "department": self.department,
            "number": self.number,
            "name": self.name,
            "teacher": self.teacher,
            "students": self.students,
            "description": self.description,
            "schedule_time": self.schedule_time,
            "schedule_days": self.schedule_days,
            "syllabus": self.syllabus,
            "assignments": self.assignments,
        }

        try:
            dict_course["_id"] = self.id
        except:
            # The id has not been initialized yet
            pass

        return dict_course 

    @staticmethod
    def from_dict(dictionary: dict) -> Course:
        return Course(
            dictionary["department"],
            dictionary["number"],
            dictionary["name"],
            dictionary["teacher"],
            dictionary["students"],
            dictionary["description"],
            dictionary["schedule_time"],
            dictionary["schedule_days"],
            dictionary["syllabus"],
            list(
                map(lambda x: Assignment.from_dict(x),
                    list(dictionary["assignments"]))
            )
            if "assignments" in dictionary
            else None,
            _id=dictionary["_id"],
        )

    def add(self):
        """Add this course to the database
        """
        db.courses.insert_one(self.to_dict())

    @staticmethod
    def delete(_id: str):
        """Delete this course from the database

        Parameters
        ----------
        _id : str
            The ID of the course
        """
        try:
            db.courses.remove({"_id": _id})
        except:
            logger.exception(f"Error while deleting course {_id}")

    def get_assignments(self) -> List[Assignment]:
        """Get the assignments for this course

        This automatically adds the attribute 'course_name' to them

        Returns
        -------
        List[Assignment]
            The assignments associated with this class
        """
        assignments = []
        for assignment in self.assignments:
            # Gets the dict object from the reference to the Firestore document
            # stored in assignment,creates an Assignment object from the
            # dictionary and then appends it to the return object
            assignment.course_name = self.name
            assignments.append(assignment)

        return assignments

    def add_assignment(self, assignment: Assignment):
        """Add an assignment to this course

        Parameters
        ----------
        assignment : Assignment
            The assignment to add
        """
        try:
            dictionary = assignment.to_dict()
            dictionary["_id"] = ObjectId()
            db.courses.find_one_and_update(
                {"_id": self._id}, {"$push": {"assignments": dictionary}}
            )
        except:
            logger.exception(
                f"Error while adding assignment {assignment._id} to course {self._id}")

    def edit_assignment(self, assignment: Assignment):
        """ Edits an assignment in this course

        Parameters
        ----------
        assigment : Assigment
            The assignment to edit
        """
        try:
            dictionary = assignment.to_dict()
            dictionary['_id'] = ObjectId(assignment.ID)
            db.classes.update_one(
                {"_id": self.ID, "assignments._id": dictionary['_id']},
                {"$set": { "assignments.$": dictionary }}
            )
        except:
            logger.exception(
                f"Error while updating assignment {assignment._id} from course {self._id}"
            )

    def delete_assignment(self, assignment_id: str):
        """Delete an assignment from this course

        Parameters
        ----------
        assignment_id : str
            The ID of the assignment
        """
        try:
            db.courses.update(
                {"_id": self._id}, {"$pull": {"assignments": {"_id": assignment_id}}}
            )
        except:
            logger.exception(
                f"Error while deleting assignment {assignment_id} from class {self._id}"
            )

    @staticmethod
    def get_by_id(_id: str) -> Course:
        """Get a course by its ID

        Parameters
        ----------
        _id : str
            The ID to search for

        Returns
        -------
        Course
            The course that was found
        """
        return Course.from_dict(db.courses.find_one({"_id": ObjectId(_id)}))

    def get_full_name(self) -> str:
        r"""Returns name in the format "SOС310 U.S. History"
        """
        return self.department + str(self.number) + " " + self.name

    def update_description(self, description: str):
        try:
            if len(description) > 0:
                self.description = description

                db.courses.find_one_and_update(
                    {"_id": self._id}, {"$set": {"description": self.description}}
                )
        except:
            logger.exception(
                f"Error while updating description {description} on class {self._id}"
            )

    def get_syllabus_name(self) -> str:
        """Get the name of the syllabus for this course

        Returns
        -------
        str
            The name of the syllabus
        """
        try:
            return self.syllabus[1]
        except IndexError:
            return None

    def update_syllabus(self, syllabus: Tuple[str, str]):
        """Update the syllabus for this course

        Parameters
        ----------
        syllabus : tuple
            The syllabus in the format (id, filename)
        """
        try:
            if syllabus[1] != "":
                self.syllabus = syllabus

                db.courses.find_one_and_update(
                    {"_id": self._id}, {"$set": {"syllabus": self.syllabus}}
                )
        except:
            logger.exception(
                f"Error while updating syllabus {self.syllabus[1]} on class {self._id}"
            )
