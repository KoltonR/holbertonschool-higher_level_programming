#!/usr/bin/python3
"""
Writes string to text file in UTF8 and returns number
of chars written
"""


def append_write(filename="", text=""):
    """
    reads file and prints it to STDOUT
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return(my_file.write(text))
