#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: dfs.py
@time: 1/16/19 7:11 PM
@desc:
"""
from queue import LifoQueue


class DFS:
    def __init__(self):
        pass

    @staticmethod
    def dfs(node):
        """
        深度优先遍历使用栈
        :param node:
        :return:
        """
        if node is None:
            return

        stack = LifoQueue()
        n_set = set()

        stack.put(node)
        n_set.add(node)
        print(node.value, end=' ')

        while not stack.empty():
            cur = stack.get()

            for n in cur.l_next[0:]:
                if n not in n_set:
                    stack.put(cur)
                    stack.put(n)
                    n_set.add(n)
                    print(n.value, end=' ')
                    break


if __name__ == '__main__':
    pass
