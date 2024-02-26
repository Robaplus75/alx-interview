#!/usr/bin/python3

""" make change func"""


def makeChange(coins, total):
    """
    makes change
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    balance = 0
    coins = sorted(coins)[::-1]
    for c in coins:
        while c <= total:
            total -= c
            balance += 1
        if (total == 0):
            return balance
    return -1
