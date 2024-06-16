#!/usr/bin/python3
""" This is a module to solve the primegame prolem ,
    and determin the winner of the game based on a given
    round number and an array of integers. """


def primes(n):
    """ reterns the prime numbers between 1 and n inclusive """
    prime = []
    separ = [True] * (n + 1)
    for g in range(2, n + 1):
        if (separ[g]):
            prime.append(g)
            for i in range(g, n + 1, g):
                separ[i] = False
    return prime


def isWinner(x, nums):
    """ determines the winer of the prime game """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
