#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: is_palindrome.py
@time: 1/12/19 10:27 AM
@desc:
"""

from link.link_list import LinkList
from queue import LifoQueue


class Palindrome:
    def __init__(self):
        self.queue = LifoQueue()

    def is_palindrome_1(self, head):
        if head is None:
            return

        cur = head
        while cur is not None:
            self.queue.put(cur)
            cur = cur.next
        cur = head

        while cur is not None:
            if cur.value != self.queue.get().value:
                return False
            cur = cur.next

        return True

    def is_palindrome_2(self, head):
        if head is None or head.next is None:
            return True

        n1 = head.next
        n2 = head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next

        while n1 is not None:
            self.queue.put(n1)
            n1 = n1.next

        n1 = head

        while not self.queue.empty():
            if n1.value != self.queue.get().value:
                return False
            n1 = n1.next

        return True

    @staticmethod
    def is_palindrome_3(head):

        """

        :param head:
        :return: 返回res, 是否为回文
        """
        if head is None or head.next is None:  # ------
            return True

        n1 = head  # -------
        n2 = head  # -------

        while n2.next is not None and n2.next.next is not None:  # ------
            n1 = n1.next
            n2 = n2.next.next

        n2 = n1.next  # n2 -> right first node
        n1.next = None  # mid.next -> None
        n3 = None

        while n2 is not None:  # right part covert
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3

        n3 = n1  # save last node
        n2 = head  # left part first node # ---------
        res = True

        while n1.next is not None and n2.next is not None:
            if n1.value != n2.value:
                res = False  # -------
                break
            n1 = n1.next  # right to middle
            n2 = n2.next  # left to middle

        n1 = n3.next
        n3.next = None

        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2

        return res  # ------


if __name__ == '__main__':
    lyst = [3, 4, 5, 6, 5, 4, 3]
    link_list = LinkList()
    link_list.create(lyst)
    palindrome = Palindrome()
    res = palindrome.is_palindrome_1(link_list.get_head())
    print('linked list is or not palindrome(need n extra space): {0}'.format(res))
    res = palindrome.is_palindrome_2(link_list.get_head())
    print('linked list is or not palindrome(need n/2 extra space): {0}'.format(res))
    res = Palindrome.is_palindrome_3(link_list.get_head())
    print('linked list is or not palindrome: {0}'.format(res))
