from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from bson import ObjectId

from api import db, root_logger as logger


class Course:
    _id : str
    def __init__(
        self,
        department: str,
        number: int,
        name: str,
        teacher: Optional[str] = None,
        students: Optional[List[str]] = None,
        description: Optional[str] = "Description",
        schedule_time: Optional[str] = None,
        schedule_days: Optional[str] = None,
        syllabus: Optional[Tuple[str, str]] = None,
        assignments: Optional[List[Assignment]] = None,
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
        self.teacher = teacher if teacher is not None else ""
        self.students = students or []
        self.description = description
        self.schedule_time = schedule_time if schedule_time is not None else ""
        self.schedule_days = schedule_days if schedule_days is not None else ""
        self.syllabus = syllabus if syllabus is not None else ()
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

    def to_dict(self) -> dict:
        dict_course = {
            "department": self.department,
            "number": self.number,
            "name": self.name,
            "teacher": ObjectId(self.teacher),
            "students": self.students,
            "description": self.description,
            "schedule_time": self.schedule_time,
            "schedule_days": self.schedule_days,
            "syllabus": self.syllabus,
            "assignments": self.assignments,
        }

        try:
            dict_course["_id"] = ObjectId(self.id)
        except:
            # The id has not been initialized yet
            pass

        return dict_course 

    @staticmethod
    def from_dict(dictionary: dict) -> Course:
        from . import Assignment, Student
        return Course(
            dictionary["department"],
            dictionary["number"],
            dictionary["name"],
            dictionary["teacher"] if "teacher" in dictionary else None,
            list(
                map(lambda x: Student.from_dict(x), list(dictionary["students"]))
            ) if "students" in dictionary else None,
            dictionary["description"] if "description" in dictionary else "Description",
            dictionary["schedule_time"] if "schedule_time" in dictionary else None,
            dictionary["schedule_days"] if "schedule_days" in dictionary else None,
            dictionary["syllabus"] if "syllabus" in dictionary else None,
            list(
                map(lambda x: Assignment.from_dict(x),
                    list(dictionary["assignments"]))
            )
            if "assignments" in dictionary
            else None,
            _id=dictionary["_id"],
        )

    def add(self) -> bool:
        """Add this course to the database
        """
        try:
            self.id = db.courses.insert_one(self.to_dict()).inserted_id
            return True
        except Exception as e:
            logger.exception(f"Error while adding course {self.to_dict()}: {e}")
            return False

    def remove(self) -> bool:
        """Remove this course from the database"""
        try:
            db.courses.remove({"_id": self.id})
            return True
        except Exception as e:
            logger.exception(f"Error while deleting course {_id}: {e}")
            return False

    def update_department(self, department: str) -> bool:
        try:
            self.department = department
            db.courses.find_one_and_update(
                {"_id": self.id, "$set": {"department": self.department}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating department {department} in class {self.id}: {e}"
            )

            return False

    def update_number(self, number: int) -> bool:
        try:
            self.number = number
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"number": self.number}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating number {number} in class {self.id}: {e}"
            )

            return False

    def update_name(self, name: str) -> bool:
        try:
            self.name = name
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"name": self.name}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating name {name} in class {self.id}: {e}"
            )

            return False

    def update_teacher(self, teacher_id: str) -> bool:
        try:
            self.teacher = teacher_id
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"teacher": ObjectId(self.teacher)}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating teacher {teacher_id} in class {self.id}: {e}"
            )

            return False

    def update_description(self, description: str) -> bool:
        try:
            self.description = description
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"description": self.description}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating description {description} in class {self.id}: {e}"
            )

            return False

    def update_schedule_time(self, schedule_time: str) -> bool:
        try:
            self.schedule_time = schedule_time
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"schedule_time": self.schedule_time}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating schedule_time {schedule_time} in class {self.id}: {e}"
            )

            return False

    def update_schedule_days(self, schedule_days: str) -> bool:
        try:
            self.schedule_days = schedule_days
            db.courses.find_one_and_update(
                {"_id": self.id}, {"$set": {"schedule_days": self.schedule_days}}
            )

            return True
        except Exception as e:
            logger.exception(
                f"Error while updating schedule_days {schedule_days} in class {self.id}: {e}"
            )

            return False

    def update_syllabus(self, syllabus: Tuple[str, str]) -> bool:
        """Update the syllabus for this course

        Parameters
        ----------
        syllabus : tuple
            The syllabus in the format (id, filename)
        """
        try:
            self.syllabus = syllabus

            db.courses.find_one_and_update(
                {"_id": self._id}, {"$set": {"syllabus": self.syllabus}}
            )

            return True
        except:
            logger.exception(
                f"Error while updating syllabus {syllabus} in class {self.id}: {e}"
            )

            return False

    def update(self, department: Optional[str] = None, number: Optional[int] = None, name: Optional[str] = None, teacher: Optional[str] = None, description: Optional[str] = None, schedule_time: Optional[str] = None, schedule_days: Optional[str] = None, syllabus : Optional[Tuple[str, str]] = None) -> bool:
        r"""Updates the course's data.

        Parameters
        ----------
        department : str, optional 
        number : str, optional
        name : str, optional
        teacher : str, optional
        description : str, optional
        schedule_time : str, optional
        schedule_days : str, optional
        syllabus : Tuple[str, str], optional

        Notes
        -----
        For all the data formats please refer to `Course.__init__` docstrings.

        **Important**: to avoid confusion, we suggest to avoid using positional parameters when calling this method.

        Returns
        -------
        bool
            `True` if all update operations were successful, `False` otherwise
        """
        parameters = locals()  # Must be first line here, do not remove

        try:
            if Course.get_by_id(self.id) is None:
                raise Exception(f"The course with id {self.id} does not exist.")
        except AttributeError:
            logger.exception(f"The property `id` does not exist for this course")
        except Exception as e:
            logger.exception(f"Error while updating a course: {e}")
    
        PARAMETER_TO_METHOD = {
            'department': self.update_department,
            'number': self.update_number,
            'name': self.update_name,
            'teacher': self.update_teacher,
            'description': self.update_description,
            'schedule_time': self.update_schedule_time,
            'schedule_days': self.update_schedule_days,
            'syllabus': self.update_syllabus 
        }

        # Go through all the parameters that are None
        for parameter, value in parameters.items() if parameter != "self" and value is not None:
            response = PARAMETER_TO_METHOD[parameter](value)
            if not response:
                logger.exception(f"Error while updating course:{self.id} attribute:{parameter} value:{value}")
                return False
        
        return True

    def get_assignments(self) -> List[Assignment]:
        """Get the assignments for this course.

        This automatically adds the attribute 'course_name' to them.

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
        assignment : Assignment
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

    @staticmethod
    def get_by_department_number(department: str, number: int) -> Course:
        """Get a course by its ID

        Parameters
        ----------
        department : str
            The course's department to look up in
        number : int
            The course number to search for

        Returns
        -------
        Course
            The course that was found
        """
        return Course.from_dict(db.courses.find_one({"department": department, "number": number}))

    def get_full_name(self) -> str:
        r"""Returns name in the format "SOС310 U.S. History"
        """
        return self.department + str(self.number) + " " + self.name

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
