#!/usr/bin/python3
"""
Student class that defines a student by public: firstname, listname, age
"""


class Student():
    """
    Studnet class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation of a Student instance """
        return vars(self)
