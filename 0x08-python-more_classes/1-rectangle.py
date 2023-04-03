#!/usr/bin/python3
""" creating of empty class """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ init function """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise Exception("height must be an integer")
        if value < 0:
            raise Exception("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise Exception("width must be an integer")
        if value < 0:
            raise Exception("width must be >= 0")
        self.__width = value
