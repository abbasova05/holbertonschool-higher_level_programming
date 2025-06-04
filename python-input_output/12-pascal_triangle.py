#!/usr/bin/python3
"""Module that defines pascal_triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Hər sətrin ilk elementi 1-dir
        last_row = triangle[i - 1]

        # Hər elementi üst sətrin iki qonşu elementinin cəmi olaraq tapırıq
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])

        row.append(1)  # Hər sətrin son elementi də 1-dir
        triangle.append(row)

    return triangle
