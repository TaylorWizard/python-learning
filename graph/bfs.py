#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: bfs.py
@time: 1/16/19 6:37 PM
@desc:
"""
from queue import Queue


class BFS:
    def __init__(self):
        pass

    @staticmethod
    def bfs(node):
        """
        宽度优先遍历
        1. 用队列
        :param node:
        :return:
        """
        queue = Queue()
        n_set = set()

        queue.put(node)
        n_set.add(node)

        while not queue.empty():
            cur_node = queue.get()
            print(cur_node.value, end=' ')
            for n in cur_node.l_next[0:]:  # 遍历当前顶点向外指向的所有顶点
                if n not in n_set:
                    queue.put(n)
                    n_set.add(n)


if __name__ == '__main__':
    pass
