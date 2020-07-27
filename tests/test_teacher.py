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

    # Please change
    # def add_assignment(self):
    #     return "cool" 