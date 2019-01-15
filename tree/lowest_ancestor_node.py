#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: lowest_ancestor_node.py
@time: 1/14/19 10:49 AM
@desc:
"""
from tree.bst import BST, Node


class LowestAncestorNode:
    def __init__(self, _root):
        self.map = {}
        if _root is not None:
            self.map.update({_root: None})

        self.set_map(_root)

    @staticmethod
    def get_lowest_ancestor_node(_root, o1, o2):
        pass

    def query_lowest_ancestor_node(self, o1, o2):
        """
        使用dict和set额外空间存储节点信息
        :return:
        """
        path = set()
        cur_o1 = o1
        while cur_o1 in self.map:
            path.add(cur_o1)
            cur_o1 = self.map.get(cur_o1)

        cur_o2 = o2
        while cur_o2 not in path:
            cur_o2 = self.map.get(cur_o2)

        return cur_o2

    def set_map(self, _root):
        if _root is None:
            return

        if _root.left is not None:
            self.map.update({_root.left: _root})
        if _root.right is not None:
            self.map.update({_root.right: _root})

        self.set_map(_root.left)
        self.set_map(_root.right)


if __name__ == '__main__':
    n_list = [17, 5, 10, 12, 35, 2, 11, 29, 38]
    bst = BST(n_list)
    root = bst.get_root()
    flag1, n1, p1 = bst.search(root, root, 2)
    flag2, n2, p2 = bst.search(root, root, 11)
    lowest_ancestor_node = LowestAncestorNode(root)
    result = lowest_ancestor_node.query_lowest_ancestor_node(n1, n2)
    print('lowest ancestor node is: {0}'.format(result.data))
