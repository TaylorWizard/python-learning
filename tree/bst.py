#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bst.py
# @Author: Gakki
# @Date  : 11/01/2019
# @Desc  : 搜索二叉树

from queue import LifoQueue

class Node:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None
        self.parent = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def get_root(self):
        return self.root

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if data > node.data:
            return self.search(node.r_child, node, data)
        else:
            return self.search(node.l_child, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)

        if not flag:
            new_node = Node(data)
            new_node.parent = n
            if data > p.data:
                p.r_child = new_node
            else:
                p.l_child = new_node

    def delete(self):
        pass

    def pre_order_recur(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order_recur(root.l_child)
        self.pre_order_recur(root.r_child)

    @staticmethod
    def pre_order_un_recur(root):
        if root is not None:
            print('pre-ordered without recursive: ', end='')
            queue = LifoQueue()
            queue.put(root)
            while not queue.empty():
                root = queue.get()
                print(root.data, end=' ')
                if root.r_child is not None:
                    queue.put(root.r_child)
                if root.l_child is not None:
                    queue.put(root.l_child)

    def in_order_recur(self, root):
        if root is None:
            return

        self.in_order_recur(root.l_child)
        print(root.data, end=' ')
        self.in_order_recur(root.r_child)

    @staticmethod
    def in_order_un_recur(root):
        if root is None:
            return

        print('\nin-ordered without recursive: ', end='')
        stack = LifoQueue()
        while not stack.empty() or root is not None:
            if root is not None:
                stack.put(root)
                root = root.l_child
            else:
                root = stack.get()
                print(root.data, end=' ')
                root = root.r_child
        print()

    def pos_order_recur(self, root):
        if root is None:
            return

        self.pos_order_recur(root.l_child)
        self.pos_order_recur(root.r_child)
        print(root.data, end=' ')


if __name__ == '__main__':
    node_lyst = [17, 5, 35, 2, 11, 29, 38]

    bst = BST(node_lyst)
    print('pre-ordered recur: ', end='')
    bst.pre_order_recur(bst.get_root())
    print('\nin-ordered recur: ', end='')
    bst.in_order_recur(bst.get_root())
    print('\npos-ordered recur: ', end='')
    bst.pos_order_recur(bst.get_root())
    print('\n=============================')

    BST.pre_order_un_recur(bst.get_root())
    BST.in_order_un_recur(bst.get_root())
