#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel


class user(BaseModel):
    """Representation of state """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
