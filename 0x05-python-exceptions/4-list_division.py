#!/usr/bin/python3

""" divides element by element 2 lists """


def list_division(my_list_1, my_list_2, list_length):
    rslt = []
    try:
        for i in range(list_length):
            try:
                v_1 = my_list_1[i]
                v_2 = my_list_2[i]
                division_rslt = v_1 / v_2
                rslt.append(division_rslt)
            except ZeroDivisionError:
                rslt.append(0)
                print("division by 0")
            except TypeError:
                rslt.append(0)
                print("wrong type")
            except IndexError:
                print("out of range")
    finally:
        return (rslt)
