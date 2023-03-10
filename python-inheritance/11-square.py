#!/usr/bin/python3
""" Square class creation """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square (arborescence: BaseGeometry -> Rectangle -> Square)"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        # initialise the square as a rectangle to use area()
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """ print the Square description """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def __repr__(self):
        """ return the Square description """
        return ("[Square] {}/{}".format(self.__size, self.__size))
