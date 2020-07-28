import unittest
from flask import current_app
from app import create_app
import os

from app.modules.classes_ import Student


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
    
    # def test_student_submission(self):
    #     self.assertTrue(self.student.add_submission(self.student.ID, "5efbe85b4aeb5d21e56fa81f", "5f08c46b901a9d46438b35ed", 
    #                                 Submission(datetime.utcnow(), "Hello", [])))