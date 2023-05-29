#!/usr/bin/python3
"""
Pascal's Triangle not using Magic 11s
"""


def pascal_triangle(n):
    """
    Returns: list of pascal's Triangle
    """
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j == i or j == 0:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        return triangle

