#!/usr/bin/python3
"""
This module implements a base class for Geometry objects,
with attribute validator functions

Raises:
    Exception: area is not implemented
    TypeError: [attribute] must be an integer
    ValueError: [attribute] ,must be greater than 0
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
