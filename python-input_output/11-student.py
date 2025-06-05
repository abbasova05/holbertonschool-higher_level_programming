#!/usr/bin/python3
"""
This module defines a Student class with serialization
and deserialization methods for JSON representation.
"""


class Student:
    """Defines a student by first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list are retrieved.
        """
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
