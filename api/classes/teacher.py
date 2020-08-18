from __future__ import annotations
from typing import Dict, List, Tuple, Union, Optional
from bson import ObjectId

from api import db
from api import root_logger as logger
from .user import User

class Teacher(User):
    _type = 'Teacher'  # Immutable

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        password: Optional[Union[bytes, str]] = None,
        courses: Optional[list] = None,
        _id: Optional[str] = None,
        calendar: Optional[list] = None,
        activated: Optional[bool] = False
    ):

        r""" Initializes a user of Teacher type.

        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        classes : list
        _id : str
        activated : bool
            The activation status of the user, by default False
        """
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, _id=_id, password=password
        )
        self.courses = courses or []
        self.calendar = calendar or []

    def __repr__(self):
        return f"<Teacher {self.id}>"

    def to_dict(self) -> Dict[str, str]:
        r"""A representation of the object in a dictionary format.
        """
        dict_user = super().to_dict()
        dict_user["courses"] = self.courses
        dict_user["calendar"] = self.calendar

        return dict_user

    @staticmethod
    def from_dict(dictionary: dict) -> Teacher:
        r"""Creates a Teacher from a dictionary.

        Parameters
        ---------
        dictionary : dict

        Returns
        -------
        Teacher
        """
        if dictionary is None:
            return None
            
        try:
            return Teacher(**dictionary)
        except Exception as e:
            logger.exception(f"Error while generating a Teacher from dictionary {dictionary}: {e}")
            return None

    def add(self) -> bool:
        r"""Adds the teacher to the DB.
        """

        try:
            self.id = db.teachers.insert_one(self.to_dict()).inserted_id
        except Exception as e:
            logger.exception(f"Error while adding Teacher {self.id}: {e}")
            return False
        else:
            return True

    def remove(self) -> bool:
        r"""Removes this teacher from the database.
        """

        try:
            db.teachers.delete_one({'_id': ObjectId(self.id)})
        except Exception as e:
            logger.exception(f"Error while removing Teacher {self.id}: {e}")
            return False
        else:
            return True

    @staticmethod
    def get_by_id(id: str) -> Teacher:
        r"""Returns a Teacher object with a specified id.

        Parameters
        ---------
        id : str
            ID to look up in the database

        Returns
        -------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"_id": ObjectId(id)}))
        except:
            logger.info(f"Error when returning Teacher by id {id}")

    @staticmethod
    def get_by_email(email: str) -> Teacher:
        r""" Returns Teacher with a specified email.
        
        Parameters
        ---------
        email : str

        Returns
        ------
        Teacher
        """
        try:
            return Teacher.from_dict(db.teachers.find_one({"email": email}))
        except:
            logger.info(f"Error when returning Teacher by email {email}")

    def get_courses() -> List[Course]:
        r"""Returns a list of the Teacher's courses

        Returns
        ------
        List[Course]
            A list of a teacher's courses, represented as tuples (course-id, course-name).
        """
        courses = list()

        for course_id in self.courses:
            courses.append(Course.get_by_id(course_id))

        return courses

    def get_calendar(self) -> List[object]:
        r"""Returns a list of the Teacher's events

        Returns
        ------
        List[object]
            A list of a teacher's events, represented as objects (title, start, end, background_color, url).
        """

        events = list()
        for event in self.calendar:
            addEvent = {
                "title": event["title"],
                "start": event["start"],
                "end": event["end"],
                "background_color": event["background_color"],
                "url": event["url"]
            }
            events.append(addEvent)
            print(addEvent)

        print(f"Returned event {events}")
        return events

    def add_calendar_event(self, event):

        print(f"Adding event {event} to teacher {self.id}")

        db.teachers.find_one_and_update(
            {"_id": ObjectId(self.id)},
            {"$push": {"calendar": event}},
        )
