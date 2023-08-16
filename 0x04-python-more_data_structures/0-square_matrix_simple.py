#!/usr/bin/python3

""" a function that computes the square value of all integers of a matrix """


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] ** 2)
        new_matrix.append(row)

    return (new_matrix)
