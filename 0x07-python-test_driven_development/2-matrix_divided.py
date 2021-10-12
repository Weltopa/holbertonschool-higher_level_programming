#!/usr/bin/python3
"""Script that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that goes through matrix and divides contents by div"""
    if len(matrix) == 0:
        return None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("""matrix must be a matrix (list of lists) \
                             of integers/floats""")
        for item in row:
            if type(item) not in [float, int]:
                raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return(list(map(lambda row:
                list(map(lambda x: round(x / div, 2), row)), matrix)))
