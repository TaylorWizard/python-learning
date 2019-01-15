#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: precursor.py
@time: 1/15/19 10:53 AM
@desc:
"""
from tree.bst import BST


class Precursor:
    def __init__(self):
        pass

    @staticmethod
    def precursor(node):
        """
        1. 节点有左子树, 那么它的先驱就是它的左子树最右边的节点
        2. 如果节点没有左子树, 那么它的先驱就往上找, 找到的它的第一个祖先节点为这个祖先节点的父节点的右节点
           就是它的先驱节点
        :param node:
        :return:
        """

        if node is None:
            return

        cur = node

        if cur.left is not None:
            cur = Precursor.get_most_right(cur.left)
            return cur
        else:
            parent = cur.parent

            while parent is not None and parent.right is not cur:
                cur = parent
                parent = cur.parent
            return parent

    @staticmethod
    def get_most_right(node):
        if node is None:
            return

        cur = node

        while cur.right is not None:
            cur = cur.right

        return cur


if __name__ == '__main__':
    n_list = [17, 5, 10, 12, 35, 2, 11, 29, 38]
    bst = BST(n_list)
    root = bst.get_root()
    flag, n, p= bst.search(root, root, 10)
    bst.in_order_un_recur(root)
    precursor = Precursor.precursor(n)
    print(precursor.data)
    f1, n1, p1 = bst.search(root, root, 38)
    precursor1 = Precursor.precursor(n1)
    print(precursor1.data)
