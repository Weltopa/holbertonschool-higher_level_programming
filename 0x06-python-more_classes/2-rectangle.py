#!/usr/bin/python3
"""Currebtly empty rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Rectangle instantiation"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """String representation of this rectangle"""
        strrep = ""
        if self.__width == 0 or self.__height == 0:
            return strrep
        strrep = ("#" * self.__width + "\n") * self.__height
        return strrep
