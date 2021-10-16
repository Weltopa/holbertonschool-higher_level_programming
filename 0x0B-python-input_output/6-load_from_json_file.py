#!/usr/bin/python3
"""Loads JSON file"""
import json


def load_from_jsonfile(filename):
    """makes obj from json"""
    with open(filename, 'r') as fil:
        return json.loads(fil.read())
