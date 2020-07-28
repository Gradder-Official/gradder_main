from api.classes.user import User
from typing import Dict, List

class Admin(User):
    USERTYPE = "Admin"

    def ___init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: list = None,
        ID: str = None
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
        classes : str
            Holds the user's classes returned by the database
        ID : str, optional
            This user's ID, set automatically if not specified
        """
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        self.classes = classes if classes is not None else list()
    
    def __repr__(self) -> str:
        r"""Represents a specific class

        Used for representing the admin class

        Returns a string labeled:
        "Admin {self.ID}"
        """
        return f"<Admin {self.ID}>"

    def to_dict(self) -> Dict:
        r"""
        Turns the admin class into a dictionary

        To read more about MongoDB go here (https://docs.mongodb.com/guides/server/introduction/)
        """
        return super().to_dict()

    @staticmethod
    def from_dict(dictionary: dict) -> Admin:
        r""" Creates an admin from a dictionary

        Takes in a dictionary then casts the specific parameters as an admin object, and it includes email, first fame, last name, _id, password
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

        return user
    
    @staticmethod
    def get_by_id(id: str) -> Admin:
        r""" Returns the admin object based on id
        
        Parameters
        ----------
        id : str
            ObjectId in the string format. 
        """
        admin = Admin.from_dict(db.admins.find_one({"_id": ObjectId(id)}))
        return admin

    @staticmethod
    def get_by_email(email: str) -> Admin:
        r"""Returns the admin object based on email
        
        Parameters
        ----------
        email : str
            String containing the email of the admin
        """
        admin = Admin.from_dict(db.admins.find_one({"email": email}))
        return admin
    
    @staticmethod
    def add_student(class_id: str, email: str):
        r""" Adds a student to a specific class

        Gets a student using their email and adds their id to their appropriate class(school class)
        
        Parameters
        ----------
        class_id : str
            The ObjectId of the class(school class) in the string format
        email: str
            The email of the student
        """
        student = Student.get_by_email(email)
        db.classes.update_one(
            {"_id": ObjectId(class_id)}, {"$push": {"students": ObjectId(student.ID)}}
        )
    
    @staticmethod
    def add_class(course: Course):
        r""" Adds a new class to the course collection

        Adds a course to the course collection with empty students, assignments, and syllabus lists
        
        Parameters
        ----------
        courses : Course
            Course object
        """
        try:
            dictionary = course.to_dict()
            dictionary["_id"] = ObjectId()
            dictionary["students"] = list()
            dictionary["assignments"] = list()
            dictionary["syllabus"] = list()
            db.classes.insert_one(dictionary)
        except BaseException as e:
            print(f"Error while adding class {course.ID}: {e}")
        
    def get_class_names(self) -> Classes:
        r""" Gets all the ObjectId's for the classes collection, along with their names

        Returns a list containing tuples of class_id, and the name of the class
        """
        classes = list()

        for class_ in db.classes.find():
            class_id = class_.get("_id")
            classes.append((class_id, Classes.get_by_id(class_id).name))

        return classes