#!/usr/bin/python3

""" Defines a Pascal Triangle fUncion """


def pascal_triangle(n):
    """
    The pascal triangle function
    Args:
        n: size
    Returns:
        a list of lists of integers representing the Pascal’s triangle of n
        Otherwise an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for idx in range(n):
        row = [1]
        if idx > 0:
            prev_row = triangle[-1]
            for i in range(idx - 1):
                row.append(prev_row[i] + prev_row[i + 1])
            row.append(1)
        triangle.append(row)

    return (triangle)
