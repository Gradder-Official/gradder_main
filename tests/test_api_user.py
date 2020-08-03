import unittest
from flask import current_app

from api import create_app
from api.classes import User


class APIUserTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

        from api import root_logger as logger
        self.logger = logger
        
        self.logger.info(self.log_message("Application set up"))


    def tearDown(self):
        self.app_context.pop()

        self.logger.info(self.log_message("Application teared down"))

    def log_message(self, message: str) -> str:
        return f"{message}"
    
    def test_create_empty_user_from_dict(self):
        user_dictionary = {
            "email": "johhnydoe@example.com",
            "first_name": "Johnny",
            "last_name": "Doe",
        }

        new_user = User.from_dict(user_dictionary)

        self.logger.info(self.log_message(f"{str(new_user)} created"))

        self.assertTrue(type(new_user).__name__ == 'User')