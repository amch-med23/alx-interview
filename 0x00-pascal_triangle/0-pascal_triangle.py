#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pacals triangle set of a given number (n)"""
    if n <= 0:
        return []

    pascal_trngl_set = [0] * n

    for i in range(n):
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_trngl_set[i - 1][j]
                b = pascal_trngl_set[i - 1][j - 1]
                new_row[j] = a + b

        pascal_trngl_set[i] = new_row

    return pascal_trngl_set
