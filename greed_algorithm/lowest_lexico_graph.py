#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: greed_algorithm.py
@time: 1/20/19 11:39 AM    sorted(l)
@desc:
"""
from functools import cmp_to_key


def compare(a, b):
    if a + b < b + a:
        return -1
    elif a + b > b + a:
        return 1
    else:
        return 0


class LowestLexiconGraph:
    def __init__(self):
        pass

    @staticmethod
    def compare(a, b):
        if a + b < b + a:
            return -1
        elif a + b > b + a:
            return 1
        else:
            return 0

    @staticmethod
    def lowest_string(str_arr):
        if str_arr is None or len(str_arr) == 0:
            return ''
        res = ''
        str_arr = sorted(str_arr, key=cmp_to_key(LowestLexiconGraph.compare))
        for s in str_arr[0:]:
            res += s

        return res


if __name__ == '__main__':
    str1 = ["jibw", "ji", "jp", "bw", "jibw"]
    result = LowestLexiconGraph.lowest_string(str1)
    print(result)

    print('=====================================')

    str2 = ['ba', 'b']
    result = LowestLexiconGraph.lowest_string(str2)
    print(result)
