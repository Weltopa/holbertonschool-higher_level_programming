#!/usr/bin/python3
"""Takes URL sends request displays value of variable"""
from requests import get
from sys import argv
if __name__ == "__main__":
    print(get(argv[1]).headers.get("X-Request-Id"))
