# Note MongoDB uses Bson

from app import db
from app.logger import logger
from app.modules._classes import User, Classes
from app.modules.student._student import Student
from app.modules.teacher._teacher import Teacher
from bson import ObjectId
from re import match


class Admin(User):
    USERTYPE = "Admin"

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: list = None,
        ID: str = None,
    ):
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
        self.classes = classes if classes is not None else list()

    def __repr__(self):
        r"""Represents a specific class

        Used for representing the admin class

        Returns a string labeled:
        "Admin {self.ID}"
        """
        return f"<Admin {self.ID}> "

    def to_json(self):
        r"""Turns a specific class into Json format

        This method is used for turning a specific class into Json Format

        Changes a dictionary to Json format
        """
        json_user = super().to_json()
        return json_user

    def to_dict(self):
        r"""
        Turns something into a dictionary, in the json format

        To read more about Json/MongoDB go here (https://docs.mongodb.com/guides/server/introduction/)
        """
        return self.to_json()

    @staticmethod
    def from_dict(dictionary: dict):
        r""" Creates an admin from a dictionary

        Takes in a dictionary then casts the specific parameters as an Admin Object, and it includes Email, First Name, Last Name, _id, Password, Secret Question
        
        Parameters
        ----------
        dictionary : dict
            Containing all information related to creating a specific admin in dictionary format
        """
        user = Admin(
            email=dictionary["email"],
            first_name=dictionary["first_name"],
            last_name=dictionary["last_name"],
            ID=str(dictionary["_id"]) if "_id" in dictionary else None,
        )
        if "password" in dictionary:
            user.set_password(dictionary["password"])

        if "secret_question" in dictionary and "secret_answer" in dictionary:
            user.set_secret_question(
                dictionary["secret_question"], dictionary["secret_answer"]
            )

        return user

    @staticmethod
    def get_by_id(id: str):
        r""" Gets the Id from the Admin dictionary

        Looks through the dictionary, using the super Admin, and gets the id 
        
        Parameters
        ----------
        id : str
            Specific ObjectId in the string format. 
        """
        return Admin.from_dict(super(Admin, Admin).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        r""" Gets the name of an admin from the Admin dictionary

        Looks through the dictionary, and finds the First and Last name of a specific Admin 
        
        Parameters
        ----------
        first_name : str
            Admin first name.
        last_name: str
            Last name of an admin 
        """
        return Admin.from_dict(
            super(Admin, Admin).get_by_name("Admin", first_name, last_name)
        )

    @staticmethod
    def get_by_email(email: str):
        r""" Gets the email

        Finds an email 
        
        Parameters
        ----------
        email : str
            String containing the email of the admin.
        """
        return Admin.from_dict(super(Admin, Admin).get_by_email(email))

    @staticmethod
    def add_student(class_id: str, email: str):
        r""" Adds a student to a specific class

        Gets a student from there specific email, and then adds that email to the specific "Class" document in the classes collection 
        
        Parameters
        ----------
        class_id : str
            The ObjectId of the specific class.
        email: str
            The email of the student
        """
        student = Student.get_by_email(email)
        db.classes.update_one(
            {"_id": ObjectId(class_id)}, {"$push": {"students": ObjectId(student.ID)}}
        )

    @staticmethod
    def add_teacher(class_id: str, email: str):
        r""" Adds a teacher to a specific class

        Gets a teacher from there unique email, and then adds that email to the specific "teacher" field(as a value) 
        in the specific "Class" document in the classes collection 
        
        Parameters
        ----------
        class_id : str
            The ObjectId of the specific class.
        email: str
            The email of the teacher
        """
        teacher = Teacher.get_by_email(email)
        db.classes.update_one(
            {"_id": ObjectId(class_id)}, {"$set": {"teacher": ObjectId(teacher.ID)}}
        )

    @staticmethod
    def add_class(classes: Classes):
        r""" Adds a new class to the classes collection

        Uses all the parameters that are necessary to create a new class and initializes them. Sets the _id, as a unique ObjectId, along with Students, Assignments, and Syllabus as empty lists
        
        Parameters
        ----------
        classes : Classes
            Just a class(meaning school class)
        """
        try:
            dictionary = classes.to_dict()
            dictionary["_id"] = ObjectId()
            dictionary["students"] = list()
            dictionary["assignments"] = list()
            dictionary["syllabus"] = list()
            db.classes.insert_one(dictionary)
        except BaseException as e:
            print(f"Error while adding class {classes.ID}: {e}")

    def get_class_names(self):
        r""" Gets all the ObjectId's for the classes collection, along with there names

        First initializes an empty list, and then loops through the entire "classes" collection, and for each document it gets the specific "_id" and then proceds to put the information inside a tuple which contains the _id, and the name of the class

        Returns a list containing tuples of class_id, and the name of the class
        """
        classes = list()

        for class_ in db.classes.find():
            class_id = class_.get("_id")
            classes.append((class_id, Classes.get_by_id(class_id).name))

        return classes

