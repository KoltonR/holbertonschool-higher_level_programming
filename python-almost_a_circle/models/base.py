#!/usr/bin/python3
"""module creating base class"""
import json


class Base:
    """base class from which all others in project will stem"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to init the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string rep"""
        return (
            "[]" if list_dictionaries is None or list_dictionaries is []
            else json.dumps(list_dictionaries)
        )

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string rep to file"""
        with open("{}.json".format(cls.__name__), "w") as f:
            newL = []
            if list_objs:
                for i in list_objs:
                    newL.append(i.to_dictionary())
            f.write(cls.to_json_string(newL))

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string"""
        return (
            [] if json_string is None or 0 else json.loads(json_string)
            )

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set already"""
        return cls(1, 1).update(**dictionary)
