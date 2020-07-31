from .user import User

class Parent(User):
    _type = 'Parent'  # Immutable

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        children: List[str] = None,
        _id: str = None
    ):
        """Initialises a user of Parent type

        Parameters
        ----------
        email : str
            The user's email
        first_name : str
            The user's first name
        last_name : str
            The user's last name
        children : List[str], optional
            The children the user has, by default None
        _id : str, optional
            The ID of the user, by default None
        """

        super().__init__(
            email=email, first_name=first_name, last_name=last_name, id=_id
        )

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

    def to_dict(self) -> Dict[str, str]:
        r"""A representation of the object in a dictionary format.
        """
        dict_user = super().to_dict()
        try:
            dict_user["children"] = self.children
        except BaseException:
            pass

        return dict_user
    
    @staticmethod
    def from_dict(dictionary: dict) -> Parent:
        r"""Creates a Parent from a dictionary.

        Parameters
        ---------
        dictionary : dict

        Returns
        -------
        Parent
        """
        return Parent(**dictionary)

    @staticmethod
    def get_by_id(id: str) -> Parent:
        r"""Returns a Parent object with a specified id.
        Parameters
        ---------
        id : str
            ID to look up in the database

        Returns
        -------
        Parent
        """
        try:
            return Parent.from_dict(db.parents.find_one({"_id": ObjectId(id)}))
        except:
            logger.info(f"Error when returning Parent by id {id}")

    @staticmethod
    def get_by_email(email: str) -> Parent:
        r""" Returns Parent with a specified email.
        
        Parameters
        ---------
        email : str

        Returns
        ------
        Parent
        """
        try:
            return Parent.from_dict(db.parents.find_one({"email": email}))
        except:
            logger.info(f"Error when returning Parent by email {email}")