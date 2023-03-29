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

    """ calculate square area """
    def area(self):
        if self.__size >= 0:
            area = self.__size ** 2
            return area

    """self.__size getter"""
    @property
    def size(self):
        return self.__size

    """self.__size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
