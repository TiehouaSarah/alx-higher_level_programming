#!/usr/bin/python3

def add_integer(a, b=98):
    """ ADDITION DE DEUX NOMBRES

     >>> add_integer(1, 2)
     3

     >>> add_integer(100, -2)
     98

     >>> add_integer(2)
     100

     >>> add_integer(100.3, -2)
     98
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
