#!/usr/bin/python3

""" prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
