#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization of Square object """

    """Function for area"""
    def area(self):
        return self.size__size ** 2

    """Getter"""
    @property
    def size(self):
        return self.__size

    """Setter"""
    @size.setter
    def size(self, size):
        """Set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
