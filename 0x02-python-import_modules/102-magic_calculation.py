#!/usr/bin/python3

""" Python bytecode challenge """


def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(4, 6):
            c = c + i
        return c
    else:
        return a - b
