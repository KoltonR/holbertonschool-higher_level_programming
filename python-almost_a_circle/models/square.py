#!/usr/bin/python3
"""module for the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """defines the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def __str__(self):
        """string & print functionality"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width

        )

    def update(self, *args, **kwargs):
        """assigns new argument to each attribute"""
        idx = 0
        for arg in args:
            idx += 1
            if idx == 1:
                self.id = arg
            if idx == 2:
                self.width = arg
            if idx == 3:
                self.x = arg
            if idx == 4:
                self.y = arg
        for key, value in kwargs.items():
            if key == "size":
                self.width = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
            if key == "id":
                self.id = value

    def to_dictionary(self):
        """returns dictionary of attributes"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
