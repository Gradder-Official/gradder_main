from . import db
from .classes import User, Subscriber


def get_user(user:User):
    user = None # get the user from the database
    return user


def add_user(user:User):
    status = False # add the user to the database and get the status
    return status


def delete_user(user:User):
    status = False # delete the user from the databse and return the status
    return status


def get_subscriber(subscriber:Subscriber):
    subscriber = None # get the subsciber from the database
    return subscriber


def add_subscriber(subsciber:Subscriber):
    status = False # add the subscriber to the database and get the status
    return status


def delete_subscriber(subsciber:Subscriber):
    status = False # delere the subscriber from the database and get the status
    return status
