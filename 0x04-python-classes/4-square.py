#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Initialization of Square object """
        self.size = size

        @property
        def size(self):
            """ Retrieves the property """
            return self.__size

        @size.setter
        def size(self, size):
            """Set size"""
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        def area(self):
            """ Returns area """
            return self.__size ** 2
