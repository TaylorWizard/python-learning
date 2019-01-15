#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: paper_folding.py
@time: 1/15/19 1:50 PM
@desc:
"""


class PaperFolding:
    def __init__(self):
        pass

    @staticmethod
    def print_all_folds(n):
        """
        打印从上到下所有折痕的方向
        :param n: 对折的次数
        :return:
        """
        PaperFolding.print_process(1, n, True)

    @staticmethod
    def print_process(i, n, down=False):
        if i > n:
            return

        PaperFolding.print_process(i + 1, n, True)
        print('down' if down else 'up', end=' ')
        PaperFolding.print_process(i + 1, n, False)


if __name__ == '__main__':
    PaperFolding.print_all_folds(3)
