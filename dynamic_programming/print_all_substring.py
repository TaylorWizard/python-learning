#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: print_all_substring.py
@time: 1/22/19 10:41 PM
@desc:
"""
import traceback


class PrintAllSubstring:
    def __init__(self):
        pass

    @staticmethod
    def print_all_substring_1(chs):
        chs_list = list(chs)
        PrintAllSubstring.process(chs_list, 0, [])

    @staticmethod
    def process(chs, i, res):
        """

        :param chs:
        :param res: 当前已经选择的所形成的列表
        :param i: 当前走到i位置，要和不要, 两条路
        :return:
        """
        if i == len(chs):
            print(''.join(res))
            return

        res_keep = res.copy()
        res_keep.append(chs[i])
        PrintAllSubstring.process(chs, i + 1, res_keep)
        res_no_include = res.copy()
        PrintAllSubstring.process(chs, i + 1, res_no_include)

    @staticmethod
    def print_all_substring_2(chs):
        chs_list = list(chs)
        PrintAllSubstring.func(chs_list, 0)

    @staticmethod
    def func(chs, i):
        """

        :param chs: 当前已经选择的所形成的列表
        :param i: 当前在i位置, 选择要和不要的路
        :return:
        """
        if i == len(chs):
            print(''.join(chs))
            return

        tmp = chs[i]
        PrintAllSubstring.func(chs, i + 1)
        chs[i] = ''
        PrintAllSubstring.func(chs, i + 1)
        chs[i] = tmp


if __name__ == '__main__':
    s = 'abc'
    PrintAllSubstring.print_all_substring_2(s)
