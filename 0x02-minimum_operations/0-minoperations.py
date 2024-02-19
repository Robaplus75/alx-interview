#!/usr/bin/python3
""" minimum operations project"""


def minOperations(num):
    """
    minoperation function
    """
    if (num < 2):
        return 0
    ops, r = 0, 2
    while r <= num:
        if num % r == 0:
            ops += r
            num = num / r
            r -= 1
        r += 1
    return ops
