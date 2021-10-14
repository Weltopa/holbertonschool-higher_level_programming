#!/usr/bin/python3
"""making class that inherits from list"""


class MyList(list):
    """Class that inherits fromlist"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
