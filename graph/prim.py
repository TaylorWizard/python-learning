#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: prim.py
@time: 1/16/19 11:58 PM
@desc: 1. 创建一个priority queue 存放每条边, 按照每条边的weight排序
       2. 创建一个hash set 存放 顶点, 用来判断顶点是否在这个集合里,
          如果不在, 说明和这个点相关的所有没有解锁的边可以被解锁,然后就添加进这个集合
       3. 创建一个result set用来存放prim生成最小图的结果
"""
from queue import PriorityQueue
from graph.graph_generator import GraphClass


class Prim:
    def __init__(self):
        pass

    @staticmethod
    def prim_mst(graph):
        priority_queue = PriorityQueue()  # 存放顶点的边，按照每条边的权重来排序
        node_find_set = set()  # 存放顶点的集合, 用来判断是否需要解锁新的边
        result = set()  # 存放prim生成最小图的结果的路径

        for node in graph.nodes.values():
            if node not in node_find_set:
                node_find_set.add(node)
                for edge in node.l_edge[0:]:
                    priority_queue.put(edge)

                while not priority_queue.empty():
                    edge = priority_queue.get()
                    to_node = edge.get_to()
                    if to_node not in node_find_set:
                        node_find_set.add(to_node)
                        result.add(edge)
                        for next_edge in to_node.l_edge[0:]:
                            priority_queue.put(next_edge)
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
    r = Prim.prim_mst(g)
    for n in r:
        print('{0} <--> {1}'.format(
            n.get_from().value, n.get_to().value),
            'weight: {weight}'.format(weight=n.get_weight()))
