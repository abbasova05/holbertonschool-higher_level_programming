#!/usr/bin/python3
"""Module that defines a function to read and print the content
of a UTF-8 text file.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
