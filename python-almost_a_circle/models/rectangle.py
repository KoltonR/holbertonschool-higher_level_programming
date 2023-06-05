#!/usr/bin/python3
"""module for rectangular model"""
from models.base import Base


class Rectangle(Base):
    """defining rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle class"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """placeholder for future comments"""
            return self.__width

        @width.setter
        def width(self, width):
            """placeholder for future comments"""
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")

            self.__width = width

        @property
        def height(self):
            """placeholder for future comments"""
            return self.__height

        @height.setter
        def height(self, height):
            """placeholder for future comments"""
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be > 0")

            self.__height = height

        @property
        def x(self):
            """placeholder for future comments"""
            return self.__x

        @x.setter
        def x(self, x):
            """placeholder for future comments"""
            if type(x) is not int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")

            self.__x = x

        @property
        def y(self):
            """placeholder for future comments"""
             return self.__y

        @y.setter
        def y(self, y):
            """placeholder for future comments"""
            if type(y) is not int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")

            self.__y = y

        def __str__(self):
            """string & print functionality"""
            return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.__x,
                self.__y, self.__width, self.__height
            )

        def area(self):
            """find area of rectangle"""
            return self.__width * self.__height

        def display(self):
            """prints the triangle in hashses"""
            print("\n" * self.__y, end="")
            for i in range(self.__height):
                print("{}{}".format(" " * self.__x, "#" * self.__width))

        def update(self, *args, **kwargs):
            """assigns new argument to each attribute"""
            idx = 0
            for arg in args:
                idx += 1
                if idx == 1:
                    self.id = arg
                if idx == 2:
                    self.__width = arg
                if idx == 3:
                    self.__height = arg
                if idx == 4:
                    self.__x = arg
                if idx == 5:
                    self.__y = arg
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value

            def to_dictionary(self):
                """returns dictionary of attributes"""
                return {
                    "id": self.id,
                    "width": self.__width,
                    "height": self.__height,
                    "x": self.__x,
                    "y": self.__y
                }
