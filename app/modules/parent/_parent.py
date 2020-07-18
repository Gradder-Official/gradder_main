from app.modules._classes import User
from app.exceptions import NoUserError
from app.modules.student._student import Student

from app import db


class Parent(User):
    USERTYPE = "Parent"

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        children: list = None,
        ID: str = None,
    ):
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)

        self.children = []
        if children is not None:
            for child in children:
                try:
                    user = Student.get_by_name(
                        first_name=child["first_name"], last_name=child["last_name"]
                    )
                    self.children.append(user.ID)
                except BaseException:
                    raise NoUserError

    def __repr__(self):
        return f"<Parent {self.ID}>"

    def to_json(self):
        json_user = super().to_json()

        try:
            json_user["children"] = self.children
        except BaseException:
            pass

        return json_user

    @staticmethod
    def from_dict(dictionary: dict):
        user = Parent(
            email=dictionary["email"],
            first_name=dictionary["first_name"],
            last_name=dictionary["last_name"],
            ID=str(dictionary["_id"]) if "_id" in dictionary else None,
        )

        if "children" in dictionary:
            children_id_list = []
            for child in dictionary["children"]:
                try:
                    user = Student.get_by_name(
                        first_name=child["first_name"], last_name=child["last_name"]
                    )
                    children_id_list.append(user.ID)
                except BaseException:
                    raise NoUserError

            user.children = children_id_list

        if "password" in dictionary:
            user.set_password(dictionary["password"])

        if "secret_question" in dictionary and "secret_answer" in dictionary:
            user.set_secret_question(
                dictionary["secret_question"], dictionary["secret_answer"]
            )

        return user

    @staticmethod
    def get_by_id(id: str):
        return Parent.from_dict(super(Parent, Parent).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        return Parent.from_dict(
            super(Parent, Parent).get_by_name("Parent", first_name, last_name)
        )

    @staticmethod
    def get_by_email(email: str):
        return Parent.from_dict(super(Parent, Parent).get_by_email(email))

    # Methods for accessing grades
