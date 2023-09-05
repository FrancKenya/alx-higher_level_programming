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
    if not (
        isinstance(matrix, list) or matrix == [] or not all(
            isinstance(row, list) for row in matrix)
        or not all((isinstance(
            element, int) or isinstance(element, float))
                for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    rslt = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return (rslt)
