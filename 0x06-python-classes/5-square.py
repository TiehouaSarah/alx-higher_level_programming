#!/usr/bin/python3
"""Declare Square class"""


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ class constructor """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        """self.__size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """self.__size setter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ calculate square area """
        if self.__size >= 0:
            area = self.__size ** 2
            return area

    def my_print(self):
        """ Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            decrementing = self.__size
            incrementing_second = 0
            while decrementing > 0:
                for n in range(self.__size):
                    print("#", end='')
                print()
                decrementing = decrementing - 1
