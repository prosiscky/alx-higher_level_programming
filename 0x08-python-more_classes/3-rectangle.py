#!/usr/bin/python3
"""A class that defines a rectangle by: (based on 2-rectangle.py)"""


class Rectangle:
    """Represents a Rectangle """

    def __init__(self, width=0, height=0):
        """Initializing the Rectangle class

            Args:
                width: width of the rectangle
                height: height of the rectangle

            Raises:
                TypesError: if width of the rectangle
                ValueError: if width is < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.__width) + (self.__height * 2)

        def __str__(self):
            """Returns a rectangle"""

            if self.__height == 0 or self.__width == 0:
                return ""
            rec = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rec += "#"
                if i < self.__height - 1:
                    rec += "\n"
            return rec
