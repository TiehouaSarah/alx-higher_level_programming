#!/usr/bin/python3
"""Creating Square class """


class Square:
    """ class constructor """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
