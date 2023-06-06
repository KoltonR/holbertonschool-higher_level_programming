#!/usr/bin/python3
"""Model 10. And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """read size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Print Str format """
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        st = st.format(self.id, self.x, self.y, self.width)
        return st

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""

        if args and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(
                            self.size,
                            self.x,
                            self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }