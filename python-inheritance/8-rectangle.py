#!/usr/bin/python3
""" check for good value value """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ Nothing useless for now """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value type """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class: rectangle (parent: BaseGeometry) """

    def __init__(self, width, height):
        """ initialisation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
