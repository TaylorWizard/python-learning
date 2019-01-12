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
        self.left = None
        self.right = None
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
            return self.search(node.right, node, data)
        else:
            return self.search(node.left, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)

        if not flag:
            new_node = Node(data)
            new_node.parent = n
            if data > p.data:
                p.right = new_node
            else:
                p.left = new_node

    def delete(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if self.root.data == data:
            self.root = None
        elif flag is False:
            print('the node you want to delete is not exist')
        else:
            if n.left is None:
                if n == p.left:
                    p.left = n.right
                else:
                    p.right = n.right
                del n
            elif n.right is None:
                if n == p.left:
                    p.left = n.left
                else:
                    p.right = n.right
                del n
            else:  # 左右子树均不为空
                pre_node = n.right
                if pre_node.left is None:
                    n.data = pre_node.data
                    n.right = pre_node.right
                    del pre_node
                else:
                    next_node = pre_node.left
                    while next_node.left is not None:
                        pre_node = next_node
                        next_node = next_node.left
                    n.data = next_node.data
                    pre_node.left = next_node.right
                    del next_node

    def pre_order_recur(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order_recur(root.left)
        self.pre_order_recur(root.right)

    @staticmethod
    def pre_order_un_recur(root):
        if root is not None:
            print('\npre-ordered without recursive: ', end='')
            queue = LifoQueue()
            queue.put(root)
            while not queue.empty():
                root = queue.get()
                print(root.data, end=' ')
                if root.right is not None:
                    queue.put(root.right)
                if root.left is not None:
                    queue.put(root.left)

    def in_order_recur(self, root):
        if root is None:
            return

        self.in_order_recur(root.left)
        print(root.data, end=' ')
        self.in_order_recur(root.right)

    @staticmethod
    def in_order_un_recur(root):
        if root is None:
            return

        print('\nin-ordered without recursive: ', end='')
        stack = LifoQueue()
        while not stack.empty() or root is not None:
            if root is not None:
                stack.put(root)
                root = root.left
            else:
                root = stack.get()
                print(root.data, end=' ')
                root = root.right
        print()

    def pos_order_recur(self, root):
        if root is None:
            return

        self.pos_order_recur(root.left)
        self.pos_order_recur(root.right)
        print(root.data, end=' ')

    @staticmethod
    def pos_order_un_recur(root):
        """

        stack_1: left right parent
        stack_2: parent right left
        need O(1) extra space
        :param root:
        :return:
        """
        if root is None:
            return
        print('pos-ordered without recur: ', end='')
        stack_1 = LifoQueue()
        stack_2 = LifoQueue()
        stack_1.put(root)
        while not stack_1.empty():
            root = stack_1.get()
            stack_2.put(root)
            if root.left is not None:
                stack_1.put(root.left)
            if root.right is not None:
                stack_1.put(root.right)

        while not stack_2.empty():
            print(stack_2.get().data, end=' ')

if __name__ == '__main__':
    node_lyst = [17, 5, 35, 2, 11, 29, 38]

    bst = BST(node_lyst)
    print('pre-ordered recur: ', end='')
    bst.pre_order_recur(bst.get_root())
    print('\nin-ordered recur: ', end='')
    bst.in_order_recur(bst.get_root())
    print('\npos-ordered recur: ', end='')
    bst.pos_order_recur(bst.get_root())

    print('\n===========================================================', end='')

    BST.pre_order_un_recur(bst.get_root())
    BST.in_order_un_recur(bst.get_root())
    BST.pos_order_un_recur(bst.get_root())