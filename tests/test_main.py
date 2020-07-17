import unittest
from flask import current_app
from app import create_app
from app.modules.auth import routes

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

    # Test cases

    def test_login_logout(self):
        response = self.login('dp@gmail.com', 'password')
        self.assertTrue(response, "Login not successful")
        response = self.logout()
        self.assertTrue(response, "Logout not successful")
        
        # TO DO: Need to test invalid usernames

    def test_landing_can_load(self):
        response = self.client.get('/')
        self.assertEqual(response.status, '200 OK', 'Landing page does not load')

    def test_login_redirects_dashboard(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status, '302 FOUND', 'Dashboard route does not redirect')
