#!/usr/bin/python3
""" check for good value value """


class Rectangle(BaseGeometry):
    """ class: rectangle (parent: BaseGeometry) """

    def __init__(self, width, height):
        """ initialisation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
