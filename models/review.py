#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This is a class responsible for the state"""
    place_id = ""
    user_id = ""
    text = ""
