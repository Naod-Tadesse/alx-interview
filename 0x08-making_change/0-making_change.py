#!/usr/bin/python3
"""
making change
"""


def makeChange(coins, total):
    """min number of coind to reach the total value"""
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
