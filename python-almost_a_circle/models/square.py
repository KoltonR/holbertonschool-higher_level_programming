#!/usr/bin/python3
""" This module writes the class Square that inherits from Rectangle class.
Rectangle inherits from Base class.
base class has public instance attribute: ''id'' """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class.
    **As reminder: a Square is a Rectangle with the same width and height**
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the Square class that
        inherits from Rectangle class.
            Args:
            size (int): The size of the square (width and height).{EQUAL}
            x (int): The x-coordinate of the square. Defaults to 0.
            y (int): The y-coordinate of the square. Defaults to 0.
            id (int, optional): An identifier for the square.
            If not provided, it will be generated automatically.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the public instance attribute:
                'size' of the Square.
            Returns:
                The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the public instance attribute:
                size' of the Square.
                Args:
                    value (int): The size of the Square.
                    Sets both width and height to the same value
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ Public instance method that returns the dictionary representation
        of a Square. This dictionary must contain:
            Returns: The dictionary representation of a Square.
            This dictionary must contain:
                 id: id of the square
                 size: size of the square
                 x: x-coordinate of the square
                 y: y-coordinate of the square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Public method that updates or assigns attributes.
        each key in the dictionary is an attribute to the instance.
        Args:
        *args (list) The list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs (dict): A dictionary of arguments - keyworded arguments
            key (str): The name of the attribute.
            value (any): The value of the attribute.
        (**kwargs must be skipped if *args exists and is not empty)
        **special handling for 'size' because it is not an actual attribute of
        the object, but a property that sets both width and height.
        When the key is 'size'
        directly set width and height to the given value.**
        """
        # Use list so we can modify the order of attrs to match args
        attributes = ['id', 'size', "x", "y"]

        if args and len(args) > 0:
            # if args is not empty assign args to attrs in order
            for index, value in enumerate(args):
                if index < len(attributes):
                    if attributes[index] == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, attributes[index], value)
        else:
            # if args is empty or None assign kwargs to attrs
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Overloading the __str__ method for the Square class.
            Returns: A string representation of a Square instance.
            [Square] (<id>) <x>/<y> - <size>
            **size can be width or height they are equal**
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
