from itertools import count


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
