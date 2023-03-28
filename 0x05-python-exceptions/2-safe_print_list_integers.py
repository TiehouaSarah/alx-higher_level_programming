#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y = 0
    z = 0
    try:
        while (z < x):
            if isinstance(my_list[z], int):
                print("{:d}".format(my_list[z]), end="")
                y = y + 1
            z = z + 1
        else:
            print()
    except IndexError:
        print("")
    return y
