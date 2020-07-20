import unittest
from flask import current_app
from app import create_app

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    # Test case helper functions

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def dashboard(self, usertype):
        return self.client.get('/dashboard', follow_redirects=True)

    def test_login_redirects_dashboard(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status, '302 FOUND', 'Dashboard route does not redirect')

    def test_login_redirects_profile(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status, '302 FOUND', 'Profile route does not redirect')

    def test_login_logout(self):

        response = self.login('dp@gmail.com', 'password')
        self.assertTrue(response, "Valid login not successful")

        response = self.logout()
        self.assertTrue(response, "Logout not successful")

        response = self.login('alekseynikanov.21@gmail.com', 'GradderTeacher2020!')
        self.assertTrue(response, "Valid login not successful")

        response = self.logout()
        self.assertTrue(response, "Logout not successful")

        response = self.login('do@gmail.com', 'password')
        self.assertEqual(response.status, '404 NOT FOUND', "Invalid email was successful")

        response = self.login('meme@gmail.com', 'misterm')
        self.assertEqual(response.status, '404 NOT FOUND', "Invalid email was successful")

        response = self.login('mrm@gmail.com', 'not misterm')
        self.assertEqual(response.status, '404 NOT FOUND', "Invalid password was successful")

        response = self.login('dp@gmail.com', 'not password')
        self.assertEqual(response.status, '404 NOT FOUND', "Invalid password was successful")
