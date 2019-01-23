#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: hanoi.py
@time: 1/22/19 6:28 PM
@desc:
"""


class Hanoi:
    def __init__(self):
        pass

    @staticmethod
    def hanoi(n):
        if n > 0:
            Hanoi.func(n, 'left', 'right', 'mid')

    @staticmethod
    def func(n, start, end, other):
        if n == 1:
            print('Move 1 from {0} to {1}'.format(start, end))
        else:
            Hanoi.func(n - 1, start, other, end)
            print('Move {i} from {start} to {end}'.format(i=n, start=start, end=end))
            Hanoi.func(n - 1, other, end, start)


if __name__ == '__main__':
    Hanoi.hanoi(2)
