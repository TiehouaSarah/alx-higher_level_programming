#!/usr/bin/python3
""" creating of empty class """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ init function """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ For Calculating Rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ For calculating Rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = (self.width + self.height) * 2
        return perimeter
