#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """min operations to find H"""

    i = 0
    j = 2
    while n > 1:
        while not n % j:
            i += j
            n /= j
        j += 1
    return i
