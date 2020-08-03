import unittest
from flask import current_app

from api import create_app


class APIStudentTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Imports have to be after app creation
        from api import root_logger as logger

        self.logger = logger
        self.logger.info(self.log_message("Application set up"))


    def tearDown(self):
        self.app_context.pop()

        self.logger.info(self.log_message("Application teared down"))

    def log_message(self, message: str) -> str:
        return f"{message}"
    
    def basic_student(self) -> 'Student':
        from api.classes import Student

        dictionary = {
            "email": "teststudent@example.com", 
            "first_name": "Student", 
            "last_name": "Test",
        }

        return Student.from_dict(dictionary)
    
    def test_create_student_from_dict(self):
        from api.classes import Student

        student = self.basic_student()

        self.assertTrue(type(student).__name__ == 'Student')
        self.logger.info("Basic student created")

    def test_add_basic_student_to_the_database(self):
        from api.classes import Student

        student = self.basic_student()
        
        self.assertTrue(student.add())
        self.logger.info("Successfully added a student to the database")

