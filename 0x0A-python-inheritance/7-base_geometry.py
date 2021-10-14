#!/usr/bin/python3
"""This file defines test class and methods"""


class BaseGeometry:
    """Class definition"""

    def area(self):
        """Throws error when not created"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks data type of value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
