#!/usr/bin/python3
"""
This module implements a Rectangle object
"""

from base import Base


class Rectangle(Base):
    """
    Rectangle implementation
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization

        Args:
            width (int): width
            height (int): heigth
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """string representation

        Returns:
            str: string
        """
        return "[Rectangle] (<{}>) <{}>/<{}> - <{}>/<{}>" \
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """width getter

        Returns:
            int: width value
        """
        return self.__width

    @property.setter
    def width(self, width):
        """width setter

        Args:
            width (int): width

        Raises:
            TypeError: width must be an integer
        """
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))
        self.__width = width

    @property
    def height(self):
        """height getter

        Returns:
            int: height
        """
        return self.__height

    @property.setter
    def height(self, height):
        """height setter

        Args:
            height (int): height
        """
        self.__height = height

    @property
    def x(self):
        """x getter

        Returns:
            int: x
        """
        return self.__x

    @property.setter
    def x(self, x):
        """x setter

        Args:
            x (int): x
        """
        self.__x = x

    @property
    def y(self):
        """y getter

        Returns:
            int: y
        """
        return self.__y

    @property.setter
    def y(self, y):
        """y setter

        Args:
            y (int): y
        """
        self.__y = y

    def area(self):
        """area

        Returns:
            int: width * height
        """
        return self.width * self.height

    def display(self):
        """prints # shape of the rectangle
        """
        print('\n'*self.y, end='')
        for l in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):
        """update rectangle attributes
        """

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]

        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)
