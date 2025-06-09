#!/usr/bin/python3
"""Define a class Square."""
import pickle


class CustomObject:
    """sadsfasdfasfasdfasfad"""
    def __init__(self, **kwargs):
        """Initialize Square with size attribute"""
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.is_student = kwargs["is_student"]

    def display(self):
        """Initialize Square with size attribute"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Initialize Square with size attribute"""
        with open(filename, "ab") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Initialize Square with size attribute"""
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return cls(data)
