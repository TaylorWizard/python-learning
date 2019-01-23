#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: median_quick.py
@time: 1/20/19 10:04 PM
@desc: 一个数据流中，随时可以取得中位数
       1. 第一次加入一个数放入大根堆
       2. 后续加入数, 需要判断这个数与大根堆和小根堆的关系:
         （1) 比大根堆堆顶小, 放入大根堆
          (2) 比大根堆堆顶大， 放入小根堆
       3. 当大根堆和小根堆的size的差到达2, size大的堆, 弹出堆顶的数放入size小的堆
       4. 如果上述步骤完成后, 当前size谁大弹谁的堆顶, 就是中位数,如果两个堆的size相等, 两个
          堆都弹出堆顶, 将弹出的两个数加相加除2, 结果就是中位数
"""
from queue import PriorityQueue
from heap_sort.heap_sort import Heap
import random


def get_median_of_array(arr):
    new_arr = list.copy(arr)
    mid = (len(arr) - 1) // 2
    new_arr.sort()
    if len(new_arr) // 2 == 0:
        return (new_arr[mid] + new_arr[mid + 1]) / 2
    else:
        return new_arr[mid]


def get_random_list(max_len, max_value):
    res = list()
    for i in range(0, max_len):
        res.append(random.randint(0, max_value))
    return res


class MedianQuick:
    def __init__(self):
        self.maxHeap = Heap(comparator=lambda x, y: x - y)
        self.minHeap = Heap(comparator=lambda x, y: y - x)

    def modify_two_heap_size(self):
        if self.maxHeap.size() == self.minHeap.size() + 2:
            self.minHeap.put(self.maxHeap.get())

        if self.minHeap.size() == self.maxHeap.size() + 2:
            self.maxHeap.put(self.minHeap.get())

    def add_number(self, number):
        if self.maxHeap.empty() or number <= self.maxHeap.peek():
            self.maxHeap.put(number)
        else:
            self.minHeap.put(number)
        self.modify_two_heap_size()

    def get_median(self):
        if (self.minHeap.size() + self.maxHeap.size()) & 1 == 0:
            return (self.minHeap.get() + self.maxHeap.get()) / 2
        # print(self.minHeap.get_list())
        return self.minHeap.get() if self.minHeap.size() > self.maxHeap.size() else self.maxHeap.get()


if __name__ == '__main__':
    for i in range(0, 2000):
        l = get_random_list(5, 30)
        median_quick = MedianQuick()
        # print(l)
        for value in l[0:]:
            median_quick.add_number(value)

        if median_quick.get_median() != get_median_of_array(l):
            print('oop....what a fuck')

