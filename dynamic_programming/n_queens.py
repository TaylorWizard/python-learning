#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: n_queens.py
@time: 1/24/19 11:06 AM
@desc: N皇后问题是指在N*N的棋盘上要摆N个皇后，要求任何两个皇后不同行、不同列， 也不在同一条斜线上。
       给定一个整数n，返回n皇后的摆法有多少种。
       n=1，返回1。
       n=2或3，2皇后和3皇后问题无论怎么摆都不行，返回0。 n=8，返回92。
"""
import timeit, time, datetime


class NQueens:
    @staticmethod
    def n_queens_1(_n):
        record = [0 for i in range(0, _n)]  # 存放每一行皇后放在了哪列
        return NQueens.process_1(0, record, _n)

    @staticmethod
    def n_queens_2(_n):
        if _n < 1 or _n > 32:
            return 0
        col_lim = -1 if _n == 32 else (1 << _n) - 1
        return NQueens.process_2(col_lim, 0, 0, 0)

    @staticmethod
    def process_1(i, record, _n):
        if i == _n:
            return 1

        res = 0
        for j in range(0, _n):
            if NQueens.is_valid(record, i, j):
                record[i] = j
                res += NQueens.process_1(i + 1, record, _n)

        return res

    @staticmethod
    def is_valid(record, i, j):
        """

        :param record:
        :param i: 当前到了哪一行, 0 - i 行都要看
        :param j: 当前想要摆放到当前行的哪一列, 尝试看能不能摆放
        :return:
        """
        for k in range(0, i):
            if record[k] == j or (abs(record[k] - j) == abs(i - k)):
                return False
        return True

    @staticmethod
    def process_2(upper_lim, col_lim, left_dia_lim, right_dia_lim):
        if upper_lim == col_lim:
            return 1

        pos = upper_lim & (~(col_lim | left_dia_lim | right_dia_lim))

        res = 0
        while pos != 0:
            most_right_one = pos & (~pos + 1)
            pos = pos - most_right_one
            res += NQueens.process_2(upper_lim, col_lim | most_right_one,
                                     (left_dia_lim | most_right_one) << 1,
                                     (right_dia_lim | most_right_one) >> 1)
        return res


if __name__ == '__main__':
    n = 8
    start = time.process_time()
    num = NQueens.n_queens_1(n)
    print(num)
    end = time.process_time()
    print('Running time %.2f seconds' % (end - start))
    print(NQueens.n_queens_2(n))
