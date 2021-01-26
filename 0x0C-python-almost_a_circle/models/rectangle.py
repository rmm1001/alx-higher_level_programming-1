#!/usr/bin/python3
"""
This module implements a base model
"""

from base import Base

class Rectangle(Base):
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id

    @property
    def width(self):
        return self.__width

    @property.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property.setter
    def height(self, height):
        self.__height = height
    @property
    def x(self):
        return  self.__x

    @property.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return  self.__y

    @property.setter
    def y(self, y):
        self.__y = y

