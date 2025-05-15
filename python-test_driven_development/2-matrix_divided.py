#!/usr/bin/python3

"""
This module is to divide two integers.

"""


def matrix_divided(matrix, div):
    """
    The function divide matrix and div:

    Returns:
    Divide of the two integers of matrix and div

    Raises:
    TypeError: if matrix or div is nto a float or integer
    TypeError: Each row of matrix must have same size
    ZeroDivisionError:if div is divided by zero
    """

    result = None
    result = int(matrix) / int(div)
    if not isinstance(matrix, (float, int)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, (float, int)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if not isinstance(div, (float, int)):
        raise ZeroDivisionError("division by zero")
    
    return result
