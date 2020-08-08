import unittest
from flask import current_app

from api import create_app


class APIStudentDatabaseOperationsTestCase(unittest.TestCase):
    r"""A testcase on all the custom database operations that can be performed with Student class.
    On `setUp`, adds a test student account to the database, which is destroyed on `tearDown`
    """
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Imports have to be after app creation
        from api import root_logger as logger
        from api.classes import Student


        self.logger = logger

        dictionary = {
            "email": "teststudent@example.com", 
            "first_name": "Student", 
            "last_name": "Test",
        }

        self.student = Student.from_dict(dictionary)
        if self.student.add():
            self.logger.info(f"Successfully created a student {self.student.id}")

    def tearDown(self):
        if self.student.remove():
            self.logger.info(f"Successfully removed a student ")

        self.app_context.pop()

    def log_message(self, message: str) -> str:
        return f"{message}"

    def test_get_student_by_id(self):
        from api.classes import Student

        self.assertIsNone(Student.get_by_id("InvalidId"))
        self.logger.info("Returned None on invalid ID")

        self.assertTrue(type(Student.get_by_id(self.student.id)).__name__ == 'Student')
        self.logger.info("Successfully retrieved a student from the database")