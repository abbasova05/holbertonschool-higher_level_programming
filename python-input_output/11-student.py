#!/usr/bin/python3
"""
This module defines a Student class.
It includes methods for serializing and deserializing instances to and from JSON format.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this list are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
