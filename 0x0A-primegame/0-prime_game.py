#!/usr/bin/python3
"""prime game project"""


def isWinner(x, nums):
    """is winner function"""
    if nums is None or (x <= 0):
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]

    a[0] = 0
    a[1] = 0

    for i in range(2, len(a)):
        remove_m(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None


def remove_m(ls, x):
    """for removing mulitple primes"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
