#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: IPO.py
@time: 1/22/19 5:26 PM
@desc:  正数数组costs
        正数数组profits
        正数k
        正数m
        含义:
            costs[i]表示i号项目的花费
            profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
            k表示你只能串行的最多做k个项目
            m表示你初始的资金
        说明: 你每做完一个项目，马上获得的收益，可以支持你去做下一个项目。 输出:
             你最后获得的最大钱数
        1. 最开始有初始资金, 创建一个花费小根堆, 一个利益大根堆
        2. 将所有项目先放进花费小根堆
        3. 用for循环来控制最多做k个项目, 每次循环里用一个while判断当前持有资金是否大于等于花费小堆根的堆顶
           如果是, 将这个项目加入到利益大根堆, 直到钱不够做下一个项目为止
        4. 弹出利益大根堆的堆顶, 得到的利益累加
        5. 重复3, 4, 如果当前做的项目个数没有达到k个, 但是当利益小根堆为空了, 这里说明没有钱做下后续的项目了
           返回当前累加的最大利益, 如果做满了k个, 返回当前累加做满k个项目的最大利益
"""
from heap_sort.heap_sort import Heap


class IPO:
    class Program:
        def __init__(self, p, c):
            self.p = p
            self.c = c

    @staticmethod
    def find_maximum_capital(costs, profits, k, m):
        min_c_q = Heap(comparator=lambda x, y: y.c - x.c)  # 花费小根堆
        max_p_q = Heap(comparator=lambda x, y: x.p - y.p)  # 利益大根堆
        programs = []
        w = m
        for i in range(0, len(costs)):
            programs.append(IPO.Program(profits[i], costs[i]))

        for program in programs[0:]:
            min_c_q.put(program)

        # print(min_c_q.get().c, min_c_q.get().c, min_c_q.get().c)

        for i in range(0, k):
            while not min_c_q.empty() and min_c_q.peek().c <= w:
                max_p_q.put(min_c_q.get())

            if max_p_q.empty():
                return w

            w += max_p_q.get().p

        return w


if __name__ == '__main__':
    c_list = [3, 6, 5]
    p_list = [7, 10, 8]
    wealth = IPO.find_maximum_capital(c_list, p_list, 3, 4)
    print(wealth)
