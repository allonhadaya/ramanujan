from sys import stdin

from cesaro import cesaro

from iterate import iterate_in_parallel

from series import garandi


def step(series, fn, n):
    for m in iterate_in_parallel(series, fn, n):
        print m
        stdin.readline()

# https://youtu.be/jcKRGpMiVTw?t=1110
step(garandi(), cesaro, 2)
