from re import match

from app.modules._classes import User


class Admin(User):
    USERTYPE = 'Admin'

    def __init__(self, email: str, first_name: str, last_name: str, ID: str = None):
        r"""Creates a user with Admin access

        This class is used for school admins that will have access to managing their school and teachers, 
        but with no access to grades or homework.

        Parameters
        ----------
        email : str
            Admin's email
        first_name : str
            Admin's first name as entered by him/herself
        last_name : str
            Admin's last name as entered by him/herself
        ID : str, optional
            This user's ID, set automatically if not specified
        """
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)

    def __repr__(self):
        return f'<Admin {self.ID}> '

    def to_json(self):
        json_user = super().to_json()
        return json_user

    def to_dict(self):
        return self.to_json()

    @staticmethod
    def from_dict(dictionary: dict):
        user = Admin(email=dictionary['email'],
                     first_name=dictionary['first_name'],
                     last_name=dictionary['last_name'],
                     ID=str(dictionary['_id']) if '_id' in dictionary else None)
        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user

    @staticmethod
    def get_by_id(id: str):
        return Admin.from_dict(super(Admin, Admin).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        return Admin.from_dict(super(Admin, Admin).get_by_name('Admin', first_name, last_name))

    @staticmethod
    def get_by_email(email: str):
        return Admin.from_dict(super(Admin, Admin).get_by_email(email))
