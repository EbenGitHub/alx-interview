#!/usr/bin/python3
"""
    0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    final_triangle = [[1] * i for i in range(1, n + 1)]
    i = 1
    while i < n:
        for j in range(1, len(final_triangle[i - 1])):
            final_triangle[i][j] = \
            final_triangle[i - 1][j] + \
            final_triangle[i - 1][j - 1]
        i += 1
    return final_triangle
