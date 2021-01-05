#!/usr/bin/python3

class Square:
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
