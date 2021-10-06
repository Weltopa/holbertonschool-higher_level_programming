#!/usr/bin/python3
"""module of stuff that does stuff"""


class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization of a Square object

        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
