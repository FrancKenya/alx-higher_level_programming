#!/usr/bin/python3

""" defines a rectangle based on the the previous task """


class Rectangle:
    """ class that defines the rectangle """

    number_of_instances = 0  # tracks instances
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        Args:
            Width and height
        Raises: Type and name errors
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join(
                [str(self.print_symbol * self.__width)] * self.__height
                )

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    def __del__(self):
        type(self).number_of_instances -= 1  # decrementing instance count
        print("Bye rectangle...")
