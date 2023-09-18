#!/usr/bin/python3

""" Define a rectangle class """

from models.base import Base


class Rectangle(Base):
    """ A rectangle class theat inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a restangle instance
        Args:
            width: width of that rectangle
            height: height of that rectangle
            x: x coordinate of that rectangle
            y: y coordinate of that rectangle
            id: id of the rectangle
        Raises:
            ValueError: if either width, height <= 0 or x, y < 0
            TypeError: if either width, height, x, y is not an int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ get the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setting the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ get the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setting the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Get the x attribute."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set the x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y attribute."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle and returns results """
        results = self.__width * self.__height
        return (results)

    def display(self):
        """ Display the rec using the # """
        if self.height == 0 or self.width == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for ht in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wt in range(self.width)]
            print("")

    def __str__(self):
        """ Return a custon representation of sting rectangle """
        i = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
        return (i)

    def update(self, *args):
        """
        Update attributes using no-keyword arguments
        Args:
           1st argument: id attribute
           2nd argument: width attribute
           3rd argument: height attribute
           4th argument: x attribute
           5th argument: y attribute
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]
