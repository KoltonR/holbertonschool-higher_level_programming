#!/usr/bin/python3
# 2-square.py
"""This defines a class Square."""


class Square:
    """This represents a square.
    
        size (int): The size of the new square.
    """
    def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

