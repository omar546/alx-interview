#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """ returns a list of lists of numbers
    representing the Pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define a row and fill the first and last index with 1
        a_row = [0] * (i + 1)
        a_row[0] = 1
        a_row[len(a_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(a_row):
                x = pascal_triangle[i - 1][j]
                y = pascal_triangle[i - 1][j - 1]
                a_row[j] = x + y

        pascal_triangle[i] = a_row

    return pascal_triangle
