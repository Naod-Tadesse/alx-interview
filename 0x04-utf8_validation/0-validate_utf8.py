#!/usr/bin/python3
"""utf8 encoding check"""
from itertools import takewhile


def to_bit(nums):
    """
    bit converter
    """
    for num in nums:
        bits = [(num & (1 << i)) != 0 for i in reversed(range(8))]
        yield bits


def validUTF8(data):
    """
    true or false
    """
    bits = to_bit(data)
    for byte in bits:
        if byte[0] == 0:
            continue

        ones = sum(takewhile(bool, byte))
        if ones >= 4:
            return False
        if ones <= 1:
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
