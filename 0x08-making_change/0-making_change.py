#!/usr/bin/python3
"""coin change problem"""


def makeChange(coins, total):
    """func that finds the minimum number of coins needed
    to make a given amount of money"""

    if total <= 0:
        return 0

    given_coins = sorted(coins, reverse=True)
    total_coins = 0

    for coin in given_coins:
        while total >= coin:
            total_coins += 1
            total -= coin
    if total == 0:
        return total_coins

    return -1
