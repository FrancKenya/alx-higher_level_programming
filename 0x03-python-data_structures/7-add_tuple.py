#!/usr/bin/python3


""" adds 2 tuples """


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    sum1 = a1 + b1
    sum2 = a2 + b2

    return (sum1, sum2)
