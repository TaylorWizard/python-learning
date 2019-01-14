#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: successor_node.py
@time: 1/14/19 11:39 PM
@desc:
"""
from tree.bst import BST
from utils.self_range import self_range


class SuccessorNode:
    def __init__(self):
        pass

    @staticmethod
    def get_successor_node(node=None):
        if node is None:
            return

        if node.right is not None:
            return SuccessorNode.get_most_left(node.right)
        else:
            cur = node
            parent = cur.parent
            while parent is not None and parent.left is not cur:
                cur = cur.parent
                parent = cur.parent
            return parent

    @staticmethod
    def get_most_left(node):
        if node is None:
            return

        cur = node
        while cur.left is not None:
            cur = node.left

        return cur


if __name__ == '__main__':
    n_list = []
    for i in self_range(4, 50, step=4):
        n_list.append(i)
    bst = BST(n_list)
    root = bst.get_root()
    bst.in_order_un_recur(root)
    flag, n, p = bst.search(root, root, 4)
    print(SuccessorNode.get_successor_node(n).data)
