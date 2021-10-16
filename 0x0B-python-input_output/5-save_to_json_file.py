#!/usr/bin/python3
"""Writes OBJ to text file"""
import json


def save_to_json_file(my_obj, filename=""):
    """function that converts obj to text using json"""
    with open(filename, 'w') as fil:
        fil.write(json.dumps(my_obj))
