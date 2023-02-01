#!/usr/bin/python3
""" This program define a rectangle """


class Rectangle:
    """ class that will define the rectangle precisely """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.number_of_instances += 1
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

    # ----------------- Create the thing to print

    def __str__(self):
        """ print the triangle """
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + str(self.print_symbol)
            if i != self.__height - 1 and self.__width != 0:
                string = string + '\n'
        return(string)

    def __repr__(self):
        """ return the triangle infos """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    # ----------------- Miscellaneous

    def __del__(self):
        """ thing happening when a class instance is deleted """
        print("Bye rectangle...")
        self.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
