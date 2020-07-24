import unittest
import os
from flask import current_app
from app import create_app
from app.modules.student._student import Student
from app.modules._classes.user import User
from app.modules._classes.submission import Submission
from app import db
from datetime import datetime

# Write Tests for everything you can think of 
# Todo: Add Parents Tests?

class BasicsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup")
        cls.app = create_app("testing")
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        print("Teardown")
        cls.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class StudentTests(unittest.TestCase):
    r"""
    This class contains tests for the Student Class 

    Make sure to document every test you write along with its purpose
    """
    def setUp(self):
        self.student = Student("testemail@gmail.com", "Te", "St")

    def test_student_created(self):
        self.student.set_password("password")
        self.student.set_secret_question("123", "123")
        self.assertTrue(self.student.add())
    
    def test_student_submission(self):
         self.assertTrue(self.student.add_submission(self.student.ID, "5efbe85b4aeb5d21e56fa81f", "5f08c46b901a9d46438b35ed", 
                                    Submission(datetime.utcnow(), "Hello", [])))


class AdminTests(unittest.TestCase):
    r"""

    Tests for Admin

    """

class TeachersTests(unittest.TestCase):
    r"""
    Teachers test
    """





if __name__=="__main__":
    unittest.main()
