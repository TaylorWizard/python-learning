#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: is_cbt.py
@time: 1/14/19 10:32 AM
@desc:
"""

from tree.bst import BST, Node
from queue import Queue


class IsCBT:
    def __init__(self):
        pass

    @staticmethod
    def is_cbt(node):
        if node is None:
            return True

        is_leaf = False  # 叶子节点开启阶段
        cur_node = node
        queue = Queue()
        queue.put(cur_node)

        while not queue.empty():
            cur_node = queue.get()
            l = cur_node.left
            r = cur_node.right

            if (is_leaf and l is not None and l is not None) or (l is None and r is not None):
                return False

            if cur_node.left is not None:
                queue.put(cur_node.left)
            if cur_node.right is not None:
                queue.put(cur_node.right)
            else:
                is_leaf = True

        return True


if __name__ == '__main__':
    node_list = [17, 5, 35, 2, 11, 29, 38]
    bst = BST(node_list)
    root = bst.get_root()
    is_cbt = IsCBT.is_cbt(root)
    print('is cbt: {0}'.format(is_cbt))

    print('==========================')

    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.right.right = Node(4)
    is_cbt = IsCBT.is_cbt(n)
    print('is cbt: {0}'.format(is_cbt))
