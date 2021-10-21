#!/usr/bin/python3
"""File for base.py"""

class Base:
    """Details for Base class"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Instantiation each had integer id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
