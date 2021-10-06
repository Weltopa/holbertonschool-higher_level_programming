#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """ Square class
    """

    def __init__(self, size=0):
        """ Initialization of Square object
        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    """Function for area"""
    def area(self, size=0):
        calc_area = self.__size ** 2
        return calc_area

    """Getter"""
    @property
    def size(self):
        return self.__size

    """Setter"""
    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value"
