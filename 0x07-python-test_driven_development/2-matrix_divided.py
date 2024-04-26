#!/usr/bin/python3

""" divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    The functiondivides  all elements of a matrix..

    Args:
        matrix (list of lists):input matrix that has numbers
        div: the divisor.

    Returns:
        list of lists: Nnew matrix that has elements placed to  2 dps.

    Raises:
        TypeError: If the matrix is not a list of lists of a number(int or f),
        if rows of the matrix are of varying sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    elif len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    elif not(isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    rslt = [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
    return rslt
