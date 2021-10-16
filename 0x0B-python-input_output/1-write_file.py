#!/usr/bin/python3
"""Writes to text file"""


def write_file(filename="", text=""):
    """Writes string to UTF"""
    with open(filename, "w") as fil:
        fil.write(text)
        return (len(text))
