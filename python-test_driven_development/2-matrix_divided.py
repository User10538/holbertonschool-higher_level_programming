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

    result = []
    for row in matrix:
        new_row =  []
        for i in row:
            new_row.append(round(i/div, 2))
        result.append(new_row)
        
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    #if not isinstance(matrix, (float, int)):
        #raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    return result
