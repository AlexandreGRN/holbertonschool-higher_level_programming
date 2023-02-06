#!/usr/bin/python3
""" check for good value value """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class: rectangle (parent: BaseGeometry) """

    def __init__(self, width, height):
        """ initialisation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ print the rectangle description """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        """ print the rectangle description """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ replace parent area object """
        return self.__width * self.__height
