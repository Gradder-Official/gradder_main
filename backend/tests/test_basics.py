import unittest
from flask import current_app
from api import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

        from api import root_logger as logger

        self.logger = logger

        self.name = "BasicsTestCase"

        self.logger.info(self.log_message("Application set up"))

    def tearDown(self):
        self.app_context.pop()

        self.logger.info(self.log_message("Application teared down"))

    def log_message(self, message: str) -> str:
        r"""Useful if we need to display specific information for all tests."""
        return f"{message}"

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])
