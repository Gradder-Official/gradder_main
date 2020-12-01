from __future__ import annotations

from datetime import datetime
from datetime import time
from typing import Union

from api import db
from api.tools.exceptions import InvalidFormatException


class Submission:
    _assignment_id: str
    _student_id: str
    _date_time_submitted: str
    _content: str
    _files: list  # TODO: determine what type exactly
    _grade: str
    _id: str

    def __init__(
        self,
        assignment_id: Union[str, ObjectId],
        student_id: Union[str, ObjectId],
        date_time_submitted: Union[datetime, str],
        content: str,
        files: Optional[list] = None,
        grade: Optional[str] = None,
        _id: Optional[Union[str, ObjectId]] = None,
    ):
        r"""Initializes the Submission object

        Parameters
        ----------
        assignment_id: str or bson.objectid.ObjectId
            The id of the assignment this submission is tied to
        student_id: str ot bson.objectid.ObjectId
            The id of a student that created this Submission
        date_time_submitted: str or datetime.datetime
            The exact time and date when an assignment was submitted (stored in utc, timezones are modified in school settings)
        content: str #TODO: determine what format it is
            Content of an assignment stored in Delta format from Quill.js
        files: list, optional
            A list of files represented as `#TODO: represented as what?`. Defaults to None
        grade: str, optional
            A grade that is of a valid format as specified in school settings. Defaults to None
        _id: str or bson.objectid.ObjectId, optional
        """
        self.assignment_id = assignment_id
        self.student_id = student_id
        self.date_time_submitted = date_time_submitted
        self.content = content
        self.files = files or list()
        self.grade = grade or str()
        if _id is not None:
            self.id = _id

    def to_dict(self) -> dict:
        dict_object = {
            "date_submitted": str(self.date_submitted),
            "content": str(self.content),
            "filenames": self.filenames,
            "student_id": self.student_id,
            "grade": self.grade,
        }
        try:
            dict_object["_id"] = ObjectId(self.id)
        except KeyError:
            logger.exception(f"The attribute 'id' does not exist yet.")

        return dict_object

    @classmethod
    def from_dict(cls, dictionary: dict) -> Submission:
        r"""Generates a Submission object from a dictionary.

        Parameters
        ----------
        dictionary : dict
            Dictionary with proper Submission parameters
        """

        return cls(**dictionary)

    @property
    def assignment_id(self) -> str:
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id: Union[str, ObjectId]):
        from . import Assignment

        try:
            if isinstance(assignment_id, str):
                ObjectId(assignment_id)
            else:
                assignment_id = str(assignment_id)
        except Exception as e:
            logger.exception(
                f"The assignment_id {id} is not of valid format (has to be either bson.objectid.ObjectId or convertible to bson.objectid.ObjectId)"
            )
            raise InvalidFormatException(
                f"The assignment_id {id} is not of valid format (has to be either bson.objectid.ObjectId or convertible to bson.objectid.ObjectId)"
            )

        try:
            if Assignment.get_by_id(assignment_id) is None:
                raise InvalidFormatException(
                    f"The assignment with provided id {id} does not exist"
                )
        except InvalidFormatException as e:
            logger.exception(f"Assignment with id {id} does not exist")
            raise e from InvalidFormatException
        except Exception as e:
            logger.exception(f"Error while retrieving Assignment with id {id}: {e}")

        self._assignment_id = assignment_id

    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, student_id: Union[str, ObjectId]):
        from . import Student

        try:
            if isinstance(student_id, str):
                ObjectId(student_id)
            else:
                student_id = str(student_id)
        except Exception as e:
            logger.exception(
                f"The student_id {id} is not of valid format (has to be either bson.objectid.ObjectId or convertible to bson.objectid.ObjectId)"
            )
            raise InvalidFormatException(
                f"The student_id {id} is not of valid format (has to be either bson.objectid.ObjectId or convertible to bson.objectid.ObjectId)"
            )

        try:
            if Student.get_by_id(student_id) is None:
                raise InvalidFormatException(
                    f"The Student with provided id {id} does not exist"
                )
        except InvalidFormatException as e:
            logger.exception(f"Student with id {id} does not exist")
            raise InvalidFormatException from e
        except Exception as e:
            logger.exception(f"Error while retrieving Student with id {id}: {e}")

        self._student_id = student_id

    @property
    def date_time_submitted(self) -> str:
        return self._date_time_submitted

    @date_time_submitted.setter
    def date_time_submitted(self, date_time_submitted: Union[datetime, str]):
        try:
            if isinstance(date_time_submitted, str):
                datetime(date_time_submitted)
            else:
                date_time_submitted = str(date_time_submitted)
        except Exception as e:
            logger.exception(
                f"date_time_submitted provided is not of a valid datetime.datetime format (got {date_time_submitted})"
            )
            raise InvalidFormatException(
                f"date_time_submitted provided is not of a valid datetime.datetime format (got {date_time_submitted})"
            )

        self._date_time_submitted = date_time_submitted

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str):
        # TODO: validate it's in valid Quill.Deltas format
        self._content = content

    @property
    def files(self) -> list:
        return self._files

    @files.setter
    def files(self, files: list):
        # TODO: validation
        self._files = files

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, grade: str):
        # Validate by checking against settings
        self._grade = grade

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: Union[str, ObjectId]):
        try:
            if isinstance(id, str):
                ObjectId(id)
            else:
                id = str(id)
        except Exception as e:
            raise InvalidFormatException(
                f"The id should be a valid bson.objectid.ObjectId string or object: {e}"
            )

        self._id = id
