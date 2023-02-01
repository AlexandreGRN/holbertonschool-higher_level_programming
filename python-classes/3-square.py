#!/usr/bin/python3
""" This program define a rectangle """


class Rectangle:
    """ class that will define the rectangle precisely """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # ----------------- Width
    @property
    def width(self):
        """ define the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        if value is None:
            raise TypeError("width must be an integer")
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # ----------------- Height
    @property
    def height(self):
        """ define the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value of height """
        if value is None:
            raise TypeError("height must be an integer")
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # ----------------- Area and perimeter calc

    def area(self):
        """ calculate the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ calculate the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    # ----------------- Print rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))