from sys import stdin

from cesaro import cesaro

from iterate import iterate_in_parallel

from series import alternating_naturals, garandi


def step(series, fn, n):
    '''Type anything to break.'''
    for m in iterate_in_parallel(series, fn, n):
        print m
        if stdin.readline() != '\n':
            return

# https://youtu.be/jcKRGpMiVTw?t=1110
step(garandi(), cesaro, 2)

# https://youtu.be/jcKRGpMiVTw?t=1392
step(alternating_naturals(), cesaro, 3)
