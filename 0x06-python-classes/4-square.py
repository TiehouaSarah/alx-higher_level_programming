#!/usr/bin/python3
class Square:
    """ class constructor """
    def __init__(self, size=0):
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
