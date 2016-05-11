from itertools import count, imap
from operator import mul


def garandi():
    '''https://oeis.org/A033999'''
    while True:
        yield 1
        yield -1


def natural():
    '''https://oeis.org/A000027'''
    result = count()
    next(result)
    return result


def alternating_naturals():
    '''https://oeis.org/A181983'''
    return imap(mul, garandi(), natural())
