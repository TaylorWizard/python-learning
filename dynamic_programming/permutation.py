#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: permutation.py
@time: 1/23/19 12:46 PM
@desc:
"""


class Permutation:
    def __init__(self):
        pass

    @staticmethod
    def permutation(chs):
        chs_list = list(chs)
        res = []
        Permutation.process(chs_list, 0, res)
        res.sort()
        return res

    @staticmethod
    def process(chs, i, res):
        """

        :param chs: 当前的一个排列
        :param res: 当前已经选择的结果列表
        :param i: 比如有3个字符全排列, i为3, 第一个位置能有i个选择, 第二个位置有i-1个选择, 第三个位置
                  有i—2个选择
        :return:
        """
        # base case
        if i == len(chs):
            res.append(''.join(chs))

        visit = []

        for j in range(i, len(chs)):
            if chs[j] not in visit:
                visit.append(chs[j])
                Permutation.swap(chs, i, j)
                Permutation.process(chs, i + 1, res)
                Permutation.swap(chs, i, j)

    @staticmethod
    def swap(chs, a, b):
        chs[a], chs[b] = chs[b], chs[a]


if __name__ == '__main__':
    result = Permutation.permutation('abbb')
    print(result)
