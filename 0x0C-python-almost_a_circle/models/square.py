#!/usr/bin/python3
"""Square class file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Actual Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation meth for squares"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of square"""
        strrep = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.width)
        return strrep
