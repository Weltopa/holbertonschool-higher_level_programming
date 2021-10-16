#!/usr/bin/python3
"""Converts JSON into python obj"""
import json


def from_json_string(my_str):
    """Converts string to object"""
    return json.loads(my_str)
