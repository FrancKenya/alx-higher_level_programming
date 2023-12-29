#!/usr/bin/python3
"""
This program  imports all functions
from the file calculator_1.py and handles basic operations.
"""

if __name__ == "__main__":
    import calculator_1
    import sys
    i = sys.argv
    if len(i) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(i[1])
    operator = i[2]
    b = int(i[3])

    if operator == '+':
        result = calculator_1.add(a, b)
    elif operator == '-':
        result = calculator_1.sub(a, b)
    elif operator == '*':
        result = calculator_1.mul(a, b)
    elif operator == '/':
        result = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
