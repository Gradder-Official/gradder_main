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
