from .classes import User, Subscriber

class DB:
    @staticmethod
    def get_last_id(usertype:str):
        if usertype == 'subscriber':
            return 1 # Get the last id from the database and increment it by one
        elif usertype == 'student':
            return 2 
        elif usertype == 'teacher':
            return 3
        elif usertype == 'parent':
            return 4
        elif usertype == 'admin':
            return 5
        else:
            return 0

    @staticmethod
    def get_user(user:User):
        user = None # get the user from the database
        return user

    @staticmethod
    def get_user_by_name(first_name:str, last_name:str):
        user = None
        return user

    @staticmethod
    def add_user(user:User):
        status = False # add the user to the database and get the status
        return status

    @staticmethod
    def delete_user(user:User):
        status = False # delete the user from the databse and return the status
        return status

    @staticmethod
    def get_subscriber(subscriber:Subscriber):
        subscriber = None # get the subsciber from the database
        return subscriber

    @staticmethod
    def add_subscriber(subsciber:Subscriber):
        status = False # add the subscriber to the database and get the status
        return status

    @staticmethod
    def delete_subscriber(subsciber:Subscriber):
        status = False # delere the subscriber from the database and get the status
        return status
