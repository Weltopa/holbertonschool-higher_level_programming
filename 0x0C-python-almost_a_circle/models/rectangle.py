#!/usr/bin/python3
"""File for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle object instantiation"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle with # to stdout"""
        for i in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")
