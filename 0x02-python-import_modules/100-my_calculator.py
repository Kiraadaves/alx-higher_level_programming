#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} {} {} = {}".format(argv[1], argv[2], b, add(argv[1], argv[3])))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(argv[1], argv[2], b, sub(argv[1], argv[3])))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(argv[1], argv[2], b, mul(argv[1], argv[3])))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(argv[1], argv[2], b, div(argv[1], argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
