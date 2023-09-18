#!/usr/bin/python3

""" Define a Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new square instance
        Args:
            size: size of the square
            x: x coordinate of the square
            y: y coordinate of the square
            id: identity of the square
        Raises:
            ValueError: if size <= 0, x < 0, or y < 0
            TypeError: if size, x, or y is not an int
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get size of the square """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a representation of the square """
        i = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
        return (i)
