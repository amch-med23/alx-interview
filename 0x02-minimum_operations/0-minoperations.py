#!/usr/bin/python3
"""
This is a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file. based on a given n value
"""


def minOperations(n):
    """
    returns min operations to get n Hs
    """
    operations = 0
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        """
        check if n could be broken into smaller parts
        """
        while n % i == 0:
            """ reduce n into a smaller part """
            n = n / i
            operations += i
    return operations
