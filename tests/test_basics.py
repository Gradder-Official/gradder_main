import unittest
from flask import current_app
from app import create_app
import os

# Write Tests for everything you can think of 
# Todo: Add Parents Tests?

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class StudentTests(unittest.TestCase):
    r"""
    This class contains tests for the Student Class 

    Make sure to document every test you write along with its purpose
    """


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
