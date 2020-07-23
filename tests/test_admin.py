import unittest
from flask import current_app
from app import create_app
import os

from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from json import dumps

from app.modules.admin import routes

# Todo: Make sure to work on Admin Tests(Database functionality(add Teachers to class/to school, add Students to class/to school, load certain pages))#


class AdminTests(unittest.TestCase):
    r"""

    Tests for Admin

    """

    # Test Case standard stuff
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    # helper function   
    def dashboard(self, usertype):
        return self.client.get('/dashboard', follow_redirects=True)
    
    def register_classes(self, department, number, name, teacher, description, schedule_time, schedule_days):
        return self.client.post('/registerClasses', data=dict(
            department=department,
            number=number,
            name=name,
            teacher=teacher,
            description=description,
            schedule_time=schedule_time,
            schedule_days=schedule_days
        ), follow_redirects=True)
    # Checking register classes

    # def test_dashboard_loading(self, usertype):
    #     response = self.client.get('/dashboard')
    #     self.assertEqual(response.status, '302 FOUND', 'Dashboard route does not redirect')

    # def registerClasses(self):
    #     response = self.register_classes('CS', '321n', 'Game Theory in CS', '5f016d7d0fcc27aa6bdffe43', 'Learning Game Theory', '09:10', '3, 4')
    #     self.assertTrue(response, "Registering Classes worked")