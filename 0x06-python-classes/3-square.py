#!/usr/bin/python3

"""Square class"""


class Square:
    """ class constructor """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    """another public method"""
    def area(self):
        if self.__size >= 0:
            area = self.__size ** 2
            return area
