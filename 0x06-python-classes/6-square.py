#!/usr/bin/python3
"""
This module defines a Square class

Its implements value and type checks for its attributes
Attributes:
    area
    my_print
"""


class Square:
    def __init__(self, size=0, position=0):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculates the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a square  with the corresponding size
        """
        for l in range(self.__size):
            print('#' * self.__size)
        else:
            print('')

    @property
    def __position(self):
        return self.__position

    @__position.setter
    def _position(self, position):
        if type(position) == tuple and len(position) == 2 and position:
            pass
