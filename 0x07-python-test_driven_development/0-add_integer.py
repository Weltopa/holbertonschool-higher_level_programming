#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Returns addition of two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
