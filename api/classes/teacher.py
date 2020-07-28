# imports
from api.classes.user import User

class Teacher(User):
    USERTYPE = "Teacher"

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        classes: list = None,
        id: str = None,
    ):

        r''' Initializes a Teacher user with information about email, first name, last name, classes and id

        Parameters
        ----------
        email: str
        first name: str
        last name: str
        classes: list
        id: str
        '''
        super().__init__(
            email=email, first_name=first_name, last_name=last_name, id=id
        )
        self.classes = classes if classes is not None else list()

    def __repr__(self):
        r""" Represents the Teacher as a string.
        """
        return f"<Teacher {self.id}>"

    def to_json(self):
        r""" Returns Teacher information in JSON form

        Return
        ------
        json_user: JSON
        """
        json_user = super().to_json()
        json_user["classes"] = self.classes
        return json_user
    
    @staticmethod
    def get_by_id(id: str):
        r""" Returns the Teacher according to ID

        Parameters
        ---------
        id: str

        Returns
        ------
        Teacher: object
        """
        return Teacher.from_dict(super(Teacher, Teacher).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        r""" Returns Teacher according to first and last name
        
        Parameters
        ---------
        first_name: str
        last_name: str

        Returns
        ------
        Teacher: object
        """
        return Teacher.from_dict(
            super(Teacher, Teacher).get_by_name("teacher", first_name, last_name)
        )
    
    @staticmethod
    def get_by_email(email: str):
        r""" Returns Teacher according to email

        Parameters
        ---------
        email: str

        Returns
        ------
        Teacher: object
        """
        return Teacher.from_dict(super(Teacher, Teacher).get_by_email(email))

    @staticmethod
    def add_student(class_id: str, email: str):
        r""" Adds a student to a class according to their email

        Parameters
        ----------
        class_id: str
        email: str
        """
        student = Student.get_by_email(email)
        db.classes.update_one(
            {"_id": ObjectId(class_id)}, {"$push": {"students": ObjectId(student.id)}}
        )

    @staticmethod
    def from_dict(dictionary: dict):
        r""" Creates a Teacher from a dictionary, with email, first name, last name, id and classes

        Parameters
        ---------
        dictionary: dict

        Returns
        -------
        Teacher: object
        """
        user = Teacher(
            email=dictionary["email"],
            first_name=dictionary["first_name"],
            last_name=dictionary["last_name"],
            id=str(dictionary["_id"]) if "_id" in dictionary else None,
            classes=dictionary["classes"] if "classes" in dictionary else None
        )

        if "password" in dictionary:
            user.set_password(dictionary["password"])

        return user

    def get_class_names(self):
        r""" Returns a list of the Teacher's classes

        Returns
        ------
        classes: list
        """
        classes = list()
        for class_ in self.classes:
            classes.append((class_, Classes.get_by_id(class_).name))
        
        return classes
