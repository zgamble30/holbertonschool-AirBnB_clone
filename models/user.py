#!/usr/bin/python3
from models.base_model import BaseModel
"""creating User class that inherits from BaseClass"""


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
