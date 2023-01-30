#!/usr/bin/python3
""" Defines a class Rectangle"""


class Rectangle:
    """ Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width(int): The width of the new rectangle
            height(int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set/get the current value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set/get the current value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the printable repesentation of the Rectangle
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
