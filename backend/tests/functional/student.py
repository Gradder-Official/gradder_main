# def test_new_student(self):
#         # Creating an empty student
#         user_dictionary = {
#             "email": "johhnydoe@example.com",
#             "first_name": "Johnny",
#             "last_name": "Doe",
#         }
#         new_user = Student.from_dict(user_dictionary)
#         self.assertTrue(type(new_user).__name__ == 'Student')
#         self.logger.info(self.log_message("New empty student created"))
#         # Setting and validating the password
#         TEST_PASSWORD = "VerySecurePassword!"
#         new_user.password = TEST_PASSWORD
#         self.assertTrue(new_user.validate_password(TEST_PASSWORD))
#         self.assertFalse(new_user.validate_password("Gibberish"))
#         self.logger.info(self.log_message("Password set correctly"))
#         # Adding a student to the database
