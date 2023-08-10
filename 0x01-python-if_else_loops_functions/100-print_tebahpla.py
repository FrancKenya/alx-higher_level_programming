#!/usr/bin/python3

for value in range(ord('Z'), ord('a') - 1, -2):
    print("{}".format(chr(value)), end="")
    if value % 2 == 0:
        value += 32
    else:
        value -= 32
