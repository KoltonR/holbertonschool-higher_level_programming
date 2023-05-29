#!/usr/bin/python3
"""
Writes string to text file in UTF8 and returns number
of chars written
"""


def write_file(filename="", text=""):
    """
    reads file and prints it to STDOUT
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return(my_file.write(text))
