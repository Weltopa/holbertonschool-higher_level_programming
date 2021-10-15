#!/usr/bin/python3
"""Reads file and prints to standard output"""


def read_file(filename=""):
    """Reads the file and prints"""
    with open(filename) as f:
        print(f.read(), end="")
