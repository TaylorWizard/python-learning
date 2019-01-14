#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: self_range.py
@time: 1/14/19 11:33 PM
@desc:
"""


def unfold(func, seed):
    def go(_func, _seed, lyst):
        res = _func(_seed)
        if isinstance(res, list):
            lyst.append(res[0])
        return go(_func, res[1], lyst) if res is not None else lyst
    return go(func, seed, [])


def self_range(_min, _max, step=1):
    return unfold(lambda x: [x, x + step] if x < _max else None, _min)
