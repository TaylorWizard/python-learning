#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: is_palindrome.py
@time: 1/12/19 10:29 PM
@desc:
"""
from tree.bst import BST, Node


class ReturnType:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


class IsBalancedTree:
    def __init__(self):
        pass

    @staticmethod
    def is_balanced(node):
        return IsBalancedTree.process(node).is_balanced

    @staticmethod
    def process(node):
        if node is None:
            return ReturnType(True, 0)

        left_data = IsBalancedTree.process(node.left)
        right_data = IsBalancedTree.process(node.right)

        height = max(left_data.height, right_data.height) + 1

        is_balanced = left_data.is_balanced and right_data.is_balanced and abs(left_data.height - right_data.height) < 2

        return ReturnType(is_balanced, height)


if __name__ == '__main__':
    node_list = [17, 5, 35, 2, 11, 29, 38]
    bst = BST(node_list)
    root = bst.get_root()
    is_b = IsBalancedTree.is_balanced(root)
    print('is balanced: {0}'.format(is_b))

    print('=========================================')
    root_n = Node(1)
    root_n.left = Node(2)
    root_n.right = Node(1)
    root_n.left.left = Node(1)
    root_n.left.left.left = Node(4)
    is_b = IsBalancedTree.is_balanced(root_n)
    print('is balanced: {0}'.format(is_b))