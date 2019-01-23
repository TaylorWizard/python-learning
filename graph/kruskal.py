#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: kruskal.py
@time: 1/17/19 12:01 AM
@desc: 1. 将graph nodes 传入到my_sets 进行初始化
       2. 创建一个优先级队列, 存放图中的每条边
       3. 创建一个 result set存放最小生成图的路径
       4. 遍历优先级队列, 判断每条边所在的from和to点是否是在同一个集合中,
          没有就添加到result里，并且合并两个顶点所在的集合
"""
from queue import PriorityQueue
from graph.graph_generator import GraphClass
from graph.my_sets import MySets


class Kruskal:
    """
    要求无向图
    """
    def __init__(self):
        pass

    @staticmethod
    def kruskal(graph):
        my_sets = MySets(list(graph.nodes.values()))
        priority_queue = PriorityQueue()
        for edge in graph.edges:
            priority_queue.put(edge)

        result = set()
        while not priority_queue.empty():
            edge = priority_queue.get()
            if not my_sets.is_same_set(edge.get_from(), edge.get_to()):
                result.add(edge)
                my_sets.union(edge.get_from(), edge.get_to())

        return result


if __name__ == '__main__':
    g_matrix = [
        [10, 5, 3],  # [weight, from, to]
        [9, 5, 4],
        [2, 6, 4],
        [5, 4, 3],
        [11, 5, 6],
        [6, 3, 1],
        [18, 1, 2],
    ]

    g = GraphClass.graph_generator(g_matrix)
    r = Kruskal.kruskal(g)

    new_g_matrix = []

    for e in r:
        print('{0} -- {1}'.format(e.get_from().value, e.get_to().value), 'weight: {0}'.format(e.get_weight()))
