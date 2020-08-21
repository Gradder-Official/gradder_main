from __future__ import annotations
from typing import Dict, List, Optional, Tuple
from bson import ObjectId
import re

from api import db
from api import root_logger as logger
from api.classes import Assignment
from api.tools.exceptions import InvalidFormatException, InvalidTypeException


class Course:
    _id : str
    _department : str
    _number : int
    _name : str
    _teacher : str
    _students : List[str]
    _description : str
    _schedule_time : str
    _schedule_days : str
    _syllabus : Tuple[str, str]
    _assignments : List[Assignment]
    _grade_range : Tuple[int, int]

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
        grade_range: Optional[Tuple[int, int]] = None,
        _id: str = None,
    ):
        """Initialises the Course object

        Parameters
        ----------
        department : str
            The department this course is under
            Format: capital alpha characters, length between 1 and 20 (ex.: "MAT", "S", "SCIENCE")
            Regex: "/[\w]{1, 20}/"
        number : int
            The course number
            Format: numerical characters, number between 0 and 100000 (ex.: 101, 002, 20005)
            Regex: "/[0-9]{1, 5}/"
        name : str
            The name of the course
            Format: alpha characters, space, and '.' allowed, length between 1 and 50 (ex. "AP U.S. History", "The Foundations of the Universe")
            Regex: "/[\w \.]{1, 100}/"
        teacher : str, optional
            The teacher giving the course, by default None
            Format: should be a valid `bson.ObjectId`, the teacher should exist in the database, teacher's department must match course's department
        students : List[str], optional
            The list of IDs of all the students in this course, by default None
            Format: should be a list of strings, each of which is a valid `bson.ObjectId`, and all students must be existent in the database
        description : str, optional
            The description of the course, by default "Description"
            Format: alphanumeric characters, space, brackets, and delimeters; length between 1 and 500 symbols
            Regex: "/[\w \.\+\(\)\[\]\{\}\?\*\&\^\%\$\#\/\'"~<>,:;!-_=@]{1, 500}/"
        schedule_time : str, optional
            The scheduled time for the course, by default None
            Format: a string, convertible to datetime.time in format `%H:%M-%H:%M` (24-hour format), in UTC
            Regex: "/[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}/"
        schedule_days : str, optional
            The scheduled days for the course, by default None
            Format: week day abbreviations from ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'] as a string.
        syllabus : Tuple[str, str], optional
            The syllabus for this course, by default None
            Format: (syllabus_id, syllabus_filename)
        assignments : List[Assignment], optional
            The assignments under this course, by default None
            Format: the list of valid `api.classes.Assignment` instances
        grade_range : Tuple[int, int], optional
            The grade range for this course, if None set to (0, 100), by default None
        _id : str, optional
            The ID of the course, by default None
            Format: string which can be converted to `bson.objectId`
        """
        self.department = department
        self.number = number
        self.name = name
        self.teacher = teacher or ""
        self.students = students or list()
        self.description = description
        self.schedule_time = schedule_time or ""
        self.schedule_days = schedule_days or ""
        self.syllabus = syllabus or tuple()
        self.assignments = assignments or list()
        self.grade_range = grade_range or (0, 100)
        if _id is not None:
            self.id = _id

    def __repr__(self):
        return f"<Course {self.id}>"

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: Union[ObjectId, str]):
        if not isinstance(id, (ObjectId, str)):
            raise InvalidTypeException(f"The id provided is not a str or bson.objectid.ObjectId (type provided is {type(id)}).")

        try:
            if isinstance(id, str):
                ObjectId(id)
            else:
                id = str(id)
        except Exception as e:
            raise InvalidFormatException(f"Cannot convert provided id to bson.ObjectId: {e}")

        self._id = id

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, department: str):
        if not isinstance(department, str):
            raise InvalidTypeException(f"The department provided is not a string (type provided is {type(department)}).")

        self._department = department

    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, number: int):
        if not isinstance(number, int):
            raise InvalidTypeException(f"The course number provided is not an int (type provided is {type(name)}).")
            
        if not 0 < number < 100000:
            raise InvalidFormatException(f"The format for course number doesn't match. Expected 0 < number < 100000, got {number}")
    
        self._number = number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise InvalidTypeException(f"The name provided is not a str (type provided is {type(name)}).")
            
        if not 0 < len(name) <= 50:
            raise InvalidFormatException(f"The length of the name should not exceed 50 characters (currently: {len(name)})")

        if not re.match('[\w \.]{1,50}', name, flags=re.UNICODE):
            raise InvalidFormatException(f"The format for the name doesn't match. Expected only alpha characters, space, or dot, got {name}")

        self._name = name

    @property
    def teacher(self) -> str:
        return self._teacher

    @teacher.setter
    def teacher(self, teacher_id: Union[str, ObjectId]):
        from api.classes import Teacher

        if isinstance(teacher_id, ObjectId):
            teacher_id = str(teacher_id)

        if not isinstance(teacher_id, str):
            raise InvalidTypeException(f"The teacher_id provided is not a str (type provided is {type(teacher)}).")
        
        if teacher_id == "":
            self._teacher = teacher_id
            return

        try:
            ObjectId(teacher_id)
        except Exception as e:
            logger.exception(f"Error while validating teacher id {teacher_id}: {e}")
            raise e

        try:
            if Teacher.get_by_id(teacher_id) is None:
                raise Exception(f"The teacher with id {teacher_id} does not exist.")
        except Exception as e:
            logger.exception(f"Error while validating the existence of teacher {teacher_id}: {e}")
            raise e

        self._teacher = teacher_id

    @property
    def students(self) -> List[Student]:
        return self._students
    
    @students.setter
    def students(self, students: List[Union[str, ObjectId]]):
        from api.classes import Student

        if not isinstance(students, list):
            raise InvalidTypeException(f"The parameter 'students' provided is not a list (type provided is {type(students)}).")

        if students == [] or students == [None]:
            self._students = list()
            return
            
        if isinstance(students[0], ObjectId):
            students = [str(student_id) for student_id in students]

        for student_id in students:
            if not isinstance(student_id, str):
                raise InvalidTypeException(f"The parameter student_id {student_id} in students is not a str (type provided is {type(student_id)}).")

            try:
                ObjectId(student_id)
            except Exception as e:
                logger.exception(f"Error while validating student id {student_id}: {e}")
                raise e

            try:
                if Student.get_by_id(student_id) is None:
                    raise Exception(f"The student with id {student_id} does not exist.")
            except Exception as e:
                logger.exception(f"Error while validating the existence of student {student_id}: {e}")
                raise e
        
        self._students = students

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise InvalidTypeException(f"The description provided is not a str (type provided is {type(description)})")

        if not 0 < len(description) <= 500:
            raise InvalidFormatException(f"The string provided is too long. The description should not exceed 500 characters. (currently: {len(description)})")

        if not re.match(r'[\w \.\+\(\)\[\]\{\}\?\*\&\^\%\$\#\/\'"~<>,:;!-_=@]{1,500}', description, flags=re.UNICODE):
            raise InvalidFormatException(r"The format for description doesn't match. Expected '[\w \.\+\(\)\[\]\{\}\?\*\&\^\%\$\#\/\'\"~<>,:;!-_=@]{1, 500}', got {description}".format(description=description))

        self._description = description

    @property
    def schedule_time(self) -> str:
        return self._schedule_time
    
    @schedule_time.setter
    def schedule_time(self, schedule_time: str):
        if not isinstance(schedule_time, str):
            raise InvalidTypeException(f"The schedule_time provided is not a str (type provided is {type(schedule_time)}")
            
        if schedule_time == "":
            self._schedule_time = ""
            return

        if not re.match(r'([0-1][0-9]|2[0-4]):[0-5][0-9]-([0-1][0-9]|2[0-4]):[0-5][0-9]', schedule_time):
            raise InvalidFormatException(f"The format for schedule_time doesn't match. Expected '([0-1][0-9] | 2[0-4]):[0-5][0-9]-([0-1][0-9] | 2[0-4]):[0-5][0-9]', got {schedule_time}")

        start_time, finish_time = schedule_time.split('-')
        start_time_h, start_time_m = list(map(int, start_time.split(':')))
        finish_time_h, finish_time_m = list(map(int, finish_time.split(':')))
        if (start_time_h*60 + start_time_m >= finish_time_h*60 + finish_time_m) and not (start_time_h == 23 and finish_time_h == 0):
            raise InvalidFormatException(f"The start time for schedule_time must be earlier than the finish time (got {schedule_time})")

        self._schedule_time = schedule_time
    
    @property
    def schedule_days(self) -> str:
        return self._schedule_days
    
    @schedule_days.setter
    def schedule_days(self, schedule_days: str):
        # TODO: make schedule days a list of weekdays abbreviated as ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        # TODO: check for type and re match
        self._schedule_days = schedule_days

    @property
    def syllabus(self) -> Tuple[str, str]:
        return self._syllabus
    
    @syllabus.setter
    def syllabus(self, syllabus: Tuple[str, str]):
        if not isinstance(syllabus, tuple):
            # TODO: logger
            raise InvalidTypeException(f"The syllabus provided is not a tuple (type provided is {type(syllabus)})")

        if syllabus == ():
            self._syllabus = syllabus
            return

        if len(syllabus) != 2 or not isinstance(syllabus[0], str) or not isinstance(syllabus[1], str):
            # TODO: logger
            raise InvalidFormatException(f"The format for syllabus does not match: expected Tuple[str, str], got {syllabus}")

        # TODO: add check for a valid syllabus
        self._syllabus = syllabus


    @property
    def grade_range(self) -> Tuple[int, int]:
        return self._grade_range
    
    @property
    def grade_range(self, grade_range: Tuple[int, int]):
        if type(grade_range) == tuple and len(grade_range) == 2:
            if grade_range[1] >= grade_range[0]:
                raise ValueError("Max value must be larger than min value for grade range")
            self._grade_range = grade_range
        else:
            raise ValueError("Grade range is not tuple or of length 2") 


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
            "grade_range": list(self.grade_range)
        }

        try:
            dict_course["_id"] = ObjectId(self.id)
        except:
            # The id has not been initialized yet
            pass

        return dict_course 

    @classmethod
    def from_dict(cls, dictionary: dict) -> Course:
        return cls(
            department=dictionary["department"],
            number=dictionary["number"],
            name=dictionary["name"],
            teacher=dictionary["teacher"] if "teacher" in dictionary else None,
            students=dictionary["students"] if "students" in dictionary else None,
            description=dictionary["description"] if "description" in dictionary else None,
            schedule_time=dictionary["schedule_time"] if "schedule_time" in dictionary else None,
            schedule_days=dictionary["schedule_days"] if "schedule_days" in dictionary else None,
            syllabus=dictionary["syllabus"] if "syllabus" in dictionary else None,
            assignments=list(
                map(lambda x: Assignment.from_dict(x),
                    list(dictionary["assignments"]))
            )
            if "assignments" in dictionary
            else None,
            grade_range=dictionary["grade_range"],
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
        r"""Updates the department of this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        department : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the course number of this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        number : int

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the name of this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        name : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the teacher for this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        teacher_id : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the description for this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        description : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the schedule time for this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        schedule_time : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the schedule days for this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        schedule_days : str

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
        """
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
        r"""Updates the syllabus for this course.

        Method should only be called on the courses that are already initialized and pushed to the DB.

        Parameters
        ----------
        syllabus : Tuple[str, str]
            The syllabus in the format (syllabus_id, syllabus_filename)

        Returns
        -------
        bool
            `True` if the update operation was successful, `False` otherwise
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
        
    def update_grade_range(self, grade_range: Tuple[int, int]) -> bool:
        """Update the grade range for this course

        Parameters
        ----------
        grade_range : Tuple[int, int]
            The grade range (min, max)

        Returns
        -------
        bool
            `True` if operation was a success. `False` otherwise
        """
        try:
            self.grade_range = grade_range

            db.courses.find_one_and_update(
                {"_id": self._id}, {"$set": {"grade_range": self.grade_range}}
            )

            return True
        except:
            logger.exception(
                f"Error while updating grade_range {grade_range} in class {self.id}: {e}"
            )

            return False

    def update(self, **kwargs) -> bool:
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
        grade_range : Tuple[int, int], option

        Returns
        -------
        bool
            `True` if all update operations were successful, `False` otherwise

        Notes
        -----
        For all the data formats please refer to `Course.__init__` docstrings.

        **Important**: to avoid confusion, we suggest to avoid using positional parameters when calling this method.
        """
        try:
            if Course.get_by_id(self.id) is None:
                raise Exception(f"The course with id {self.id} does not exist.")
        except AttributeError:
            logger.exception(f"The property `id` does not exist for this course")
            return False
        except Exception as e:
            logger.exception(f"Error while updating a course")
            return False
    
        PARAMETER_TO_METHOD = {
            'department': self.update_department,
            'number': self.update_number,
            'name': self.update_name,
            'teacher': self.update_teacher,
            'description': self.update_description,
            'schedule_time': self.update_schedule_time,
            'schedule_days': self.update_schedule_days,
            'syllabus': self.update_syllabus,
            'grade_range': self.update_grade_range
        }

        # Go through all the parameters that are None
        for key, value in kwargs.items():
            response = PARAMETER_TO_METHOD[key](value)
            if not response:
                logger.exception(f"Error while updating course:{self.id} attribute: {key} value: {value}")
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
