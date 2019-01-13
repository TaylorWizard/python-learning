#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: small_equal_bigger.py
@time: 1/13/19 3:22 PM
@desc:
"""
from link.link_list import LinkList


class SmallEqualBigger:
    @staticmethod
    def small_equal_bigger_1(head, pivot):
        if head is None or head.next is None:
            return

        sH, sT = None, None  # 小于区域
        eH, eT = None, None  # 等于区域
        bH, bT = None, None  # 大于区域
        next = None
        while head is not None:
            next = head.next
            head.next = None
            if head.value < pivot:
                if sT is None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            if head.value == pivot:
                if eT is None:
                    eH = head
                    eT = head
                else:
                    eT.next = head
                    eT = head
            if head.value > pivot:
                if bH is None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            head = next
        if sT is not None:
            sT.next = eH
            eT = eT if eT is not None else sT
        if eT is not None:
            eT.next = bH

        return sH if sH is not None else eH if eH is not None else bH

    @staticmethod
    def swap(node_lyst, x, y):
        node_lyst[x], node_lyst[y] = node_lyst[y], node_lyst[x]

    @staticmethod
    def small_equal_bigger_2(head, pivot):
        if head is None and head.next is None:
            return

        lyst = []
        while head is not None:
            lyst.append(head)
            head = head.next

        left = -1
        right = len(lyst)
        index = 0

        while index != right:
            if lyst[index].value < pivot:
                left += 1
                SmallEqualBigger.swap(lyst, index, left)
                index += 1
            elif lyst[index].value == pivot:
                index += 1
            else:
                right -= 1
                SmallEqualBigger.swap(lyst, index, right)

        i = 1
        for i in range(i, len(lyst)):
            lyst[i - 1].next = lyst[i]

        lyst[i].next = None

        return lyst


if __name__ == '__main__':
    linklist = LinkList()
    lyst = [3, 5, 1, 9, 2, 0, 5]
    linklist.create(lyst)

    head_node = SmallEqualBigger.small_equal_bigger_1(linklist.get_head(), 5)
    while head_node is not None:
        print(head_node.value, end=' ')
        head_node = head_node.next

    print('\n======================================')

    node_list = SmallEqualBigger.small_equal_bigger_2(linklist.get_head(), 5)
    for node in node_list[0:]:
        print(node.value, end=' ')
