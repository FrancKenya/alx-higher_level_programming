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

    @size.setter
    def size(self, value):
        """ Validate size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square attributes from *args and **kwargs
        Args:
            args: New attribute values.
                1st argument: represents id attribute
                2nd argument: represents size attribute
                3rd argument: represents x attribute
                4th argument: represents y attribute
        kwargs: A dict storing key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is not None:
                        self.id = arg
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns a dictiionary representation of the square """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
