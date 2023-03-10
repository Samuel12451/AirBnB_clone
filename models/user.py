#!/usr/bin/python3

"""
A module that defines a User class which inherits BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines all common attribute/methods for other classes
    Attributes:
        id
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
