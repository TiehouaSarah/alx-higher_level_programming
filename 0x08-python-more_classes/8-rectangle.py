#!/usr/bin/python3
""" creating of empty class """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init function """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ returning variable containing rectangle to print"""
        line_to_print = ""

        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)

        if self.width == 0 or self.height == 0:
            return line_to_print

        for n in range(self.height):
            line_to_print += self.print_symbol * self.width
            if n is not self.height - 1:
                line_to_print += "\n"
        return line_to_print

    def __repr__(self):
        """ string representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Detect instance deletion """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2
