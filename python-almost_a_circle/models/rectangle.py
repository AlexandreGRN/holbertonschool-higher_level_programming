#!/usr/bin/python3
""" Creating rectangle Class """
from base import Base


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
        self.__width = value

    # ---------- Height
    @property
    def height(self):
        """ get the height value """
        return self.__height
    
    @width.setter
    def height(self, value):
        """ set the height value to @height """
        self.__height = value
