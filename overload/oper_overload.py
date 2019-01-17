#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: oper_overload.py
@time: 1/17/19 3:32 PM
@desc:
"""


class OverLoad:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        print('__lt__')
        return self.priority < other.priority

    def __add__(self, other):
        print('__add__: ', end='')
        return OverLoad(self.priority + other.priority, self.description)

    def __str__(self):
        return 'Vector (%d %s)' % (self.priority, self.description)


if __name__ == '__main__':
    o1 = OverLoad(10, 'o1')
    o2 = OverLoad(20, 'o2')
    print(o1 + o2)  # o1 + o2 调用 __add__, print 调用 __str__
    if o1 < o2:  # 调用 __it__
        print('o1 < o2')
