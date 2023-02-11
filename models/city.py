#!/usr/bin/python3

"""A module that defines a City class which inherits BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name(str)
        state_id(str)
    """
    name = ""
    state_id = ""
