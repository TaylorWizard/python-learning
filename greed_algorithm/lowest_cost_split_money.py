#!/usr/bin/env python
# encoding: utf-8
"""
@author: gakki
@software: garner
@file: lowest_cost_split_money.py
@time: 1/22/19 2:20 PM
@desc: 使用到huffman tree
"""
from heap_sort.heap_sort import Heap


class LowestCostSplitMoney:
    def __init__(self, l_split):
        self.min_heap = Heap(comparator=lambda x, y: y - x)
        self.l_split = l_split

    def less_money(self):
        _sum = 0

        for value in self.l_split[0:]:
            self.min_heap.put(value)

        while self.min_heap.size() > 1:
            cur = self.min_heap.get() + self.min_heap.get()
            _sum += cur
            self.min_heap.put(cur)

        return _sum


if __name__ == '__main__':
    l = [6, 7, 8, 9]
    lcsm = LowestCostSplitMoney(l)
    result = lcsm.less_money()
    print(result)
