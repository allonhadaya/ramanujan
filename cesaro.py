def partial_sum(series):

    s = 0
    for n in series:
        s += n
        yield s


def partial_average(series):

    series = iter(series)
    n = next(series)
    yield n

    depth = 1.0

    for m in series:
        depth += 1
        n = n * ((depth - 1) / depth) + m / depth
        yield n


def cesaro(series):
    '''https://en.wikipedia.org/wiki/Ces%C3%A0ro_summation'''
    return partial_average(partial_sum(series))
