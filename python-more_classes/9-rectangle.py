#!/usr/bin/python3
"""
Write an class Rectangle that defines a rectangle with width and height
Add print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
"""


class Rectangle:
    """
    Write an class Rectangle that defines a rectangle with width and height.
    Add print() and str() should print the rectangle with the character #:
    if width or height is equal to 0, return an empty string


    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        # Increment on instantiation
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        # Convert the class or instance-level print_symbol to a string
        # This ensures that even if it's a number or other
        # type, it will work correctly
        symbol = str(self.print_symbol)

        lines = []
        for i in range(self.height):
            # Each line is made by repeating the symbol
            # for the width of the rectangle
            line = symbol * self.width
            lines.append(line)
        rectangle_string = "\n".join(lines)

        return rectangle_string

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")

        # Decrement on instantiation
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    # This is a static method
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        # calls the constructor with both width
        # and height equal to size
        return cls(size, size)
