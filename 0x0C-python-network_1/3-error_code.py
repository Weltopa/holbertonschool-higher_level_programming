#!/usr/bin/python3
"""Script that sends request to URL"""
from sys import argv as av
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(av[1]) as response:
            print(response.read().decode("utf-8"))

    except HTTPError as err:
        print("Error code: {}".format(err.code))
