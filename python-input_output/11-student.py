#!/usr/bin/python3
"""Student class that can be serialized to and deserialized from JSON."""

class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize Student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, return all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the values in json.

        Args:
            json (dict): Dictionary with keys as attribute names and values as new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value) 
