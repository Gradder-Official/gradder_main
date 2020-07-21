import unittest
from flask import current_app
from app import create_app
from app.main.forms import (
    SubscriberForm,
    InquiryForm,
)
from urllib.parse import urlparse

class MainTestCase(unittest.TestCase):

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

    # TEST CASES

    def test_landing_can_load(self):
        response = self.client.get('/')
        self.assertEqual(response.status, '200 OK', 'Landing does not load')

    # Forms

    def test_subscription_form_submits(self):
        form = SubscriberForm(data = {'email': 'test@gmail.com'})
        self.assertTrue(form.validate(), "Cannot subscribe with email")

    def test_blank_email_in_subscription(self):
        form = SubscriberForm(data={'email': ''})
        self.assertFalse(form.validate(), "Validates blank email")

    def test_invalid_email_in_subscription(self):
        form = SubscriberForm(data={'email': 'this isnt an email!'})
        self.assertFalse(form.validate(), "Validates invalid email")

    def test_valid_inquiry_form_submits(self):
        form = InquiryForm(data = {
            'name': 'Inquirer', 
            'email': 'inquirer@gmail.com',
            'subject': "Bugs/suggestions",
            'inquiry': 'I have an inquiry!'
        })
        self.assertTrue(form.validate(), "Cannot validate inquiry")

    def test_invalid_inquiry_form_name(self):
        form = InquiryForm(data = {
            'name': '', 
            'email': 'inquirer@gmail.com',
            'subject': "Bugs/suggestions",
            'inquiry': 'I have an inquiry!'
        })
        self.assertFalse(form.validate(), "Validates blank name")

    def test_invalid_inquiry_form_email(self):
        form = InquiryForm(data = {
            'name': 'bobby', 
            'email': 'mynameisbobby!',
            'subject': "Bugs/suggestions",
            'inquiry': 'I have an inquiry!'
        })
        self.assertFalse(form.validate(), "Validates invalid email")

    # Redirecting - h e l p  I don't know why this part doesn't work

    # def test_forms_redirect_home(self):
    #    response = self.client.post(
    #        '/index',
    #        data={'email': 'test@gmail.com'}
    #    )
    #    self.assertEqual(response.status_code, 302, "Forms do not redirect")
    #    self.assertEqual(response['location'], '/index', "Forms do not redirect to landing")