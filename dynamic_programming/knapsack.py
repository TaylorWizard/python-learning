#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: knapsack.py
@time: 1/23/19 11:02 PM
@desc:
"""


class Knapsack:
    @staticmethod
    def greatest_value(weights, values, bag):
        return Knapsack.process(weights, values, 0, 0, bag)

    @staticmethod
    def process(weights, values, i, already_weight, bag):
        if i == len(weights):
            return 0

        if already_weight + weights[i] > bag:
            return 0
        else:
            return max(Knapsack.process(weights, values, i + 1, already_weight, bag),
                       Knapsack.process(weights, values, i + 1, already_weight + weights[i], bag) + values[i])


if __name__ == '__main__':
    w_list = [10, 5, 20, 15, 35]
    v_list = [5, 25, 24, 12, 29]
    print(Knapsack.greatest_value(w_list, v_list, 10))
