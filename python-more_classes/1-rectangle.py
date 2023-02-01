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
