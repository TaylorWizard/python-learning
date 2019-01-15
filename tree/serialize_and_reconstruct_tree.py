#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: serialize_and_reconstruct_tree.py
@time: 1/15/19 11:00 PM
@desc:
"""
from tree.bst import BST, Node
from queue import Queue


class SerializeAndReconstructTree:
    def __init__(self):
        pass

    @staticmethod
    def serialize_by_pre(head):
        if head is None:
            return '#_'

        res = str(head.data) + '_'
        res += SerializeAndReconstructTree.serialize_by_pre(head.left)
        res += SerializeAndReconstructTree.serialize_by_pre(head.right)

        return res

    @staticmethod
    def reconstruct_by_pre_string(pre_str):
        values = pre_str.split('_')
        queue = Queue()

        for i in range(0, len(values)):
            queue.put(values[i])

        return SerializeAndReconstructTree.recon_by_pre_order(queue)

    @staticmethod
    def recon_by_pre_order(queue):
        value = queue.get()

        if value == '#':
            return None

        head = Node(int(value))
        head.left = SerializeAndReconstructTree.recon_by_pre_order(queue)
        head.right = SerializeAndReconstructTree.recon_by_pre_order(queue)

        return head


if __name__ == '__main__':
    sat = SerializeAndReconstructTree()
    n_list = [17, 5, 35, 2, 11, 29, 38]
    bst = BST(n_list)
    root = bst.get_root()
    str_tree = SerializeAndReconstructTree.serialize_by_pre(root)
    print('serialized tree: ', str_tree)

    print('reconstructed tree: ', end='')
    recon_tree = SerializeAndReconstructTree.reconstruct_by_pre_string(str_tree)
    bst.pre_order_un_recur(recon_tree)

