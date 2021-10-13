#!/usr/bin/python3
"""Prints text with two new lines after each: ., ?, :"""


def text_indentation(text):
    """checks if string then replaces accordingly"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    newtext = text.replace('?', '?\n\n')
    newtext = newtext.replace('.', '.\n\n')
    newtext = newtext.replace(':', ':\n\n')
    print("\n".join([item.strip() for item in newtext.split("\n")]), end="")
