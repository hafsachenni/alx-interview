#!/usr/bin/python3
"""prime game task"""


def prime_game(n):
    """function that returns ints from 1 up to
     and including n"""
    prime_nums = []
    isnum_prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if isnum_prime[num]:
            prime_nums.append(num)
            for i in range(num, n + 1, num):
                isnum_prime[i] = False
    return prime_nums


def isWinner(x, nums):
    """function that determines who the winner is"""
    if not x or not nums:
        return None

    maria_winner, ben_winner = 0, 0
    for play_round in nums[:x]:
        prime_nums = prime_game(play_round)
        if len(prime_nums) % 2 == 0:
            ben_winner += 1
        else:
            maria_winner += 1
    if maria_winner > ben_winner:
        return "Maria"
    if ben_winner > maria_winner:
        return "Ben"
    return None
