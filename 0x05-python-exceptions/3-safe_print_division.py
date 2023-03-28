#!/usr/bin/python3
def safe_print_division(a, b):
    y = 0
    try:
        y = "{:d}".format(a // b)
    except (ValueError, ZeroDivisionError):
        y = None
    finally:
        print("Inside result: {}".format(y))
    return y
