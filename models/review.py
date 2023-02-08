#!/usr/bin/python3
"""AirBnB Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines attributes/methods for the Review class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

   
