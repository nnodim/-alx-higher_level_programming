#!/usr/bin/python3
"""Module 8-rectangle
This Module contains an definition for Rectangle class
"""


class Rectangle:
    """A class to represent a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a rectangle with width and height
        Args:
            width (int, optional): width of the rect. Defaults to 0.
            height (int, optional): height of the rect. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter
        Args:
            value (int): value
        Raises:
            TypeError: if width is not an int
            ValueError: if width is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter
        Args:
            value (int): value
        Raises:
            TypeError: if height is not an int
            ValueError: if height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle
        Returns:
            int: area
        """
        return self.height * self.width

    def perimeter(self):
        """calculates the perimeter of the rectangle
        Returns:
            int: perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns a string representation of the rectangle"""
        rec_str = ""
        if (self.width == 0 or self.height == 0):
            return rec_str

        rows = [str(self.print_symbol) *
                self.width for _ in range(self.height)]
        rec_str = "\n".join(rows)
        return rec_str

    def __repr__(self):
        """returns a reproducible object representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """runs with the rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares to rectangles and returns the bigger in area
        if they are equal the first rectangle is returned
        Args:
            rect_1 (Rectangle): the first rect
            rect_2 (Rectangle): the second rect
        Raises:
            TypeError: if any of the rect is not instance of Rectangle
        Returns:
            Rectangle: the bigger rect in Area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_2 if rect_2.area() > rect_1.area() else rect_1

