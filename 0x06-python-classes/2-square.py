#!/usr/bin/python3
"""
This module defines a Square class

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0
"""


class Square:
    """This class is a class for a square model
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def __size(self):
        return self.__size

    @__size.setter
    def __size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
