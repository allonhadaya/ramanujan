from itertools import islice, izip, tee


def iterate(series, fn):
    '''(series, fn(series), fn(fn(series)), ...) where series is an iterable'''
    a = series
    while True:
        a, b = tee(a)
        yield a
        a = fn(b)


def take(n, iterable):
    '''The n first members of iterable.'''
    return list(islice(iterable, n))


def iterate_in_parallel(series, fn, n):
    '''The first n iterations of fn over series as an n-tuple iterable.'''
    return izip(*take(n, iterate(series, fn)))
