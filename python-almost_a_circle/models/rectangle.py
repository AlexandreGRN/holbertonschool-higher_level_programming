#!/usr/bin/python3
""" Creating rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # ---------- Width
    @property
    def width(self):
        """ get the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width value to @width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # ---------- Height
    @property
    def height(self):
        """ get the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height value to @height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # ---------- x
    @property
    def x(self):
        """ get the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x value to @x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # ---------- y
    @property
    def y(self):
        """ get the height value """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the height value to @height """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
