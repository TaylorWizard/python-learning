#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: topology.py
@time: 1/16/19 10:58 PM
@desc: 拓扑排序
"""
from queue import Queue


class Topology:
    def __init__(self):
        pass

    @staticmethod
    def topology(graph):
        """

        1. 创建一个hash map 和 一个 zero_in_queue,
           hash map键为每个顶点, 值为它的入度, zero_in queue 存放入度为0的顶点
        2. 创建一个 result 数组, 这个数组存放排好序的顶点
        3. 从zero in queue 弹出一个顶点, 当zero in queue 弹出一个顶点的时候将该顶点放入result
        4. 遍历弹出的顶点的l_next(自己向外指向的所有点), 并且将遍历到的next顶点放入map, 放入的入度减1
        5. 如果当前next顶点的入度为0，放入zero in queue
        6. 重复3 4 5 步骤
        :param graph: 图
        :return: result 数组, 为排好序的顶点的数组
        """

        zero_in_queue = Queue()
        in_degree_map = {}

        for node in graph.nodes.values():
            in_degree_map.update({node: node.in_degree})
            if node.in_degree == 0:
                zero_in_queue.put(node)

        result = []
        while not zero_in_queue.empty():
            cur = zero_in_queue.get()
            result.append(cur)
            for n in cur.l_next[0:]:
                in_degree_map.update({n: in_degree_map.get(n) - 1})
                if in_degree_map.get(n) == 0:
                    zero_in_queue.put(n)

        return result


if __name__ == '__main__':
    pass
