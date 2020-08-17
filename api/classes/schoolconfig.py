from __future__ import annotations

from api import db
from api import root_logger as logger


# ToDO:
# Add the proper methods for SchoolConfig
# Do we need an ObjectId, and discuss other technical details
class SchoolConfig: 
    # Add attributes and methods to edit db.general_info
    def __init__(
        self,
        school_name: str,
        school_address: str,
        phone_number: str,
        school_email: str,
        principal: str,
        principal_email: str,
        departments: List[str],
        department_description: List[str],
        grade_weights: bool,
        grading: List[str]
    ):
        """
        Helps with SchoolConfig

        Parameters
        ------------
        school_name: str
            Updating the name of the school

        school_address: str
            Address of the school

        phone_number: str,
            Phone Number of the school

        school_email: str,
            Email address of the school

        principal: str,
            The Current principal at the school

        principal_email: str,
            Email of the current principal of the school
        
        departments: List[str],
            A List of 3-letter abbreivations of the departments at the school
        
        department_description: List[str]
            List of descriptions for each department in the school
        
        grade_weights: bool,
            For the school, decides if there is a weight or not(True == Weight, False == No Weight)
        
        grading: List[str],
            Grading System for the school(Can be Letter Grades(A-F))
        """
    self._school_name = school_name
    self._school_address = school_address
    self._phone_number = phone_number
    self._school_email = school_email
    self._principal = principal
    self._departments = departments 
    self._department_description = department_description
    self._grade_weights = grade_weights 
    self._grading = grading 

    
