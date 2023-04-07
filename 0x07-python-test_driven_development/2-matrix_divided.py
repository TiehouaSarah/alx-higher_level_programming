#!/usr/bin/python3
""" Write a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if type(row) != list or len(row) != row_len:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        row_result = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix " /
                                "(list of lists) of integers/floats")
            cal = round(elem / div, 2)
            row_result.append(cal)
            if elem == row[-1]:
                new_matrix.append(row_result)
    return new_matrix
