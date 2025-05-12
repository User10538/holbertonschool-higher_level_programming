#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
# loop through row in matrix
    for row in matrix:
        square_row = []
# loop through element
        for x in row:
            square_row.append(x ** 2)
        new_matrix.append(square_row)

    return new_matrix
