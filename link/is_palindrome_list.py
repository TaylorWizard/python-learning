#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 123.py
# @Author: Gakki
# @Date  : 10/01/2019
# @Desc  :


# palindrome.py
from queue import LifoQueue
from link.link_list import LinkList, Node


class Palindrome:
    def __init__(self):
        self.queue = LifoQueue()

    # need n extra space of stack
    def is_palindrome_1(self, head):
        cur = head
        while cur is not None:
            self.queue.put(cur)
            cur = cur.next

        while head is not None:
            if head.value != self.queue.get().value:
                return False
            head = head.next

        return True

    def is_palindrome_2(self, head):
        """

        使用快慢指针, 额外n/2的空间
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return True
        right = head.next
        cur = head
        while cur.next is not None and cur.next.next is not None:
            cur = cur.next.next
            right = right.next

        while right is not None:
            self.queue.put(right)
            right = right.next

        while not self.queue.empty():
            if head.value != self.queue.get().value:
                return False
            head = head.next

        return True

    @staticmethod
    def is_palindrome_3(head):
        """

        :param head: 链表的头节点
        :return:
        """
        if head is None or head.next is None:
            return True

        n1 = head
        n2 = head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next  # n2 -> right part first node
        n1.next = None  # mid.next -> null
        n3 = None

        while n2 is not None:  # right part convert
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3

        n3 = n1  # save last node
        n2 = head  # left part first node
        res = True

        while n1 is not None and n2 is not None:
            if n1.value != n2.value:
                res = False
                break
            n1 = n1.next  # right to mid
            n2 = n2.next  # left to mid

        n1 = n3.next
        n3.next = None

        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2

        return res


if __name__ == '__main__':
    lyst = [1, 2, 3, 4, 3, 2, 1]
    link_list = LinkList()
    link_list.create(lyst)
    palindrome = Palindrome()
    print('result of palindrome 1: ', palindrome.is_palindrome_1(link_list.get_head()))
    print('result of palindrome 2: ', palindrome.is_palindrome_2(link_list.get_head()))
    print('result of palindrome 3: ', Palindrome.is_palindrome_3(link_list.get_head()))

    print('=================================')

    lyst_2 = [1, 2, 3, 4, 5, 6]
    link_list_2 = LinkList()
    link_list_2.create(lyst_2)
    print('result of palindrome 1: ', palindrome.is_palindrome_1(link_list_2.get_head()))
    print('result of palindrome 2: ', palindrome.is_palindrome_2(link_list_2.get_head()))
    print('result of palindrome 3: ', Palindrome.is_palindrome_3(link_list_2.get_head()))