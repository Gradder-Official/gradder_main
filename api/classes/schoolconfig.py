from __future__ import annotations
from typing import Dict, List, Optional, Tuple

from api import db
from api import root_logger as logger
from api.tools.exceptions import InvalidFormatException, InvalidTypeException


# ToDO:
# Add the proper methods for SchoolConfig
# Do we need an ObjectId, and discuss other technical details
class SchoolConfig: 
    # Add attributes and methods to edit db.general_info
    def __init__(
        self,
        school_name: Optional[str] = None,
        school_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        school_email: Optional[str] = None,
        principal: Optional[str] = None,
        principal_email: Optional[str] = None,
        departments: Optional[list] = None,
        department_description: Optional[list] = None,
        grade_weights: Optional[bool] = None,
        grading: Optional[list] = None,
    ):
        """
        Helps with SchoolConfig

        Parameters
        ------------
        school_name: str, optional
            Updating the name of the school

        school_address: str, optional
            Address of the school

        phone_number: str, optional
            Phone Number of the school

        school_email: str, optional
            Email address of the school

        principal: str, optional
            The Current principal at the school

        principal_email: str, optional
            Email of the current principal of the school
        
        departments: List[str], optional
            A List of 3-letter abbreivations of the departments at the school
        
        department_description: List[str], optional
            List of descriptions for each department in the school
        
        grade_weights: bool, optional
            For the school, decides if there is a weight or not(True == Weight, False == No Weight)
        
        grading: List[str], optional
            Grading System for the school(Can be Letter Grades(A-F))
        """
    self._school_name = school_name or ""
    self._school_address = school_address or ""
    self._phone_number = phone_number or ""
    self._school_email = school_email or ""
    self._principal = principal or ""
    self._departments = departments or List()
    self._department_description = department_description or List()
    self._grade_weights = grade_weights 
    self._grading = grading or List()

    @property
    def school_name(self) -> str:
        return self._school_name

    @school_name.setter
    def school_name(self, school_name: str):
        if not isinstance(school_name, str):
            raise InvalidTypeException(

        f"The school name provided is not a str (type provided is {type(school_name)})."
        )

        if not 0 < len(school_name) <= 100:
            raise InvalidFormatException(
        
        f"The length of the school name should not exceed 100 characters (currently: {len(school_name)})"
        )

        if not re.match('[\w \.]{1,50}', school_name, flags=re.UNICODE):
            raise InvalidFormatException(
        
        f"The format for the name doesn't match. Expected only alpha characters, space, or dot, got {school_name}"
        )
        
        self._school_name = school_name

    @property
    def school_address(self) -> str:
        return self._school_address

    @school_address.setter
    def school_address(self, school_address: str):
        if not isinstance(school_address, str):
            raise InvalidTypeException(
        
        f"The school address provided is not a str (type provided is {type(school_address)})."
        )
        
        self._school_address = school_address

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def school_name(self, phone_number: str):
        if not isinstance(phone_number, str):
            raise InvalidTypeException(
        
        f"The phone number provided is not a str (type provided is {type(phone_number)})."
        )
        
        self._phone_number = phone_number
    
    @property
    def school_email(self) -> str:
        return self._school_email

    @school_email.setter
    def school_name(self, school_email: str):
        if not isinstance(school_email, str):
            raise InvalidTypeException(
        
        f"The school email provided is not a str (type provided is {type(school_email)})."
        )

        if not re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", school_email):
            raise InvalidTypeException(
        
        f"The school email provided is not a valid email."
        )
        
        self._school_email = school_email

    @property
    def principal(self) -> str:
        return self._principal

    @principal.setter
    def principal(self, principal: str):
        if not isinstance(principal, str):
            raise InvalidTypeException(
        
        f"The principal name provided is not a str (type provided is {type(principal)})."
        )

        if not 0 < len(principal) <= 100:
            raise InvalidFormatException(
        
        f"The length of the name should not exceed 100 characters (currently: {len(principal)})"
        )

        if not re.match('[\w \.]{1,50}', name, flags=re.UNICODE):
            raise InvalidFormatException(
        
        f"The format for the name doesn't match. Expected only alpha characters, space, or dot, got {principal}"
        )
        
        self._principal = principal

    @property
    def principal_email(self) -> str:
        return self._principal_email

    @principal_email.setter
    def school_name(self, principal_email: str):
        if not isinstance(principal_email, str):
            raise InvalidTypeException(
        
        f"The principal's email provided is not a str (type provided is {type(principal_email)})."
        )

        if not re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", principal_email):
            raise InvalidTypeException(
        
        f"The principal's email provided is not a valid email."
        )
        
        self._principal_email = principal_email

    @property
    def departments(self) -> List:
        return self._departments

    @departments.setter
    def departments(self, departments: list):
        if not isinstance(departments, list):
            raise InvalidTypeException(
        
        f"The departments provided are not a list (type provided is {type(departments)})."
        )
        
        self._departments = departments
    
    @property
    def department_description(self) -> List:
        return self._department_description

    @department_description.setter
    def department_description(self, department_description: list):
        if not isinstance(department_description, list):
            raise InvalidTypeException(
        
        f"The department descriptions provided are not a list (type provided is {type(department_description)})."
        )
        
        self._department_description = department_description

    @property
    def grade_weights(self) -> bool:
        return self._grade_weights

    @grade_weights.setter
    def grade_weights(self, grade_weights: bool):
        if not isinstance(self, grade_weights, bool):
            raise InvalidTypeException(
        
        f"The grade weights provided is not a boolean (type provided is {type(department_description)})."
        )

        self._grade_weights = grade_weights

    @property
    def grading(self) -> List:
        return self._grading

    @grading.setter
    def grading(self, grading: list):
        if not isinstance(grading, list):
            raise InvalidTypeException(
        
        f"The grading provided is not a list (type provided is {type(grading)})."
        )
        
        self._grading = grading

    def to_dict(self) -> dict:
        dict_school = {
            "school_name": self.school_name,
            "school_address": self.school_address,
            "phone_number": self.phone_number,
            "school_email": self.school_email,
            "principal": self.principal,
            "principal_email": self.principal_email,
            "departments": self.departments,
            "department_description": self.department_description,
            "grade_weights": self.grade_weights,
            "grading": self.grading,
        }

        return dict_school

    def from_dict(cls, dictionary: dict) -> SchoolConfig:
        return SchoolConfig(
           school_name=dictionary["school_name"] if "school_name" in dictionary else None,
           school_address=dictionary["school_address"] if "school_address" in dictionary else None,
           phone_number=dictionary["phone_number"] if "phone_number" in dictionary else None,
           school_email=dictionary["school_email"] if "school_email" in dictionary else None,
           principal=dictionary["principal"] if "principal" in dictionary else None,
           principal_email=dictionary["principal_email"] if "principal_email" in dictionary else None, 
           departments=dictionary["departments"] if "departments" in dictionary else None,
           department_description=dictionary["department_description"] if "department_description" in dictionary else None,
           grade_weights=dictionary["grade_weights"] if "grade_weights" in dictionary else None,
           grading=dictionary["grading"] if "grading" in dictionary else None
        )


    