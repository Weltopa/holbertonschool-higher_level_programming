#1/usr/bin/python3
"""Function that checks instance of class"""


def inherits_from(obj, a_class):
    """returns false if class and obj are same"""
    if type(obj) is a_class:
        return false
    return (issubclass(type(obj), a_class))
