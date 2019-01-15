#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: matrix_traverse.py
@time: 1/15/19 7:58 PM
@desc:
"""


def transpose_matrix(_matrix):
    if type(_matrix) == list and type(_matrix[0]) == list:
        return [[row[i] for row in _matrix] for i in range(0, len(_matrix[0]))]
    else:
        return None


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print(transpose_matrix(matrix))







