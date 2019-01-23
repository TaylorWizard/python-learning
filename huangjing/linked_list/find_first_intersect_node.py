#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: find_first_intersect_node.py
@time: 1/19/19 10:17 PM
@desc:
"""
from link.link_list import LinkList


class FindFirstIntersectNode:
    def __init__(self):
        pass

    @staticmethod
    def get_loop_node(head):
        """
        :param head:
        :return: 判断链表是否有环,有环返回第一个入环节点，无环返回None
        """
        if head is None or head.next is None or head.next.next is None:
            return

        slow = head.next
        fast = head.next.next
        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

    @staticmethod
    def get_intersect_node(head1, head2):
        """
        :param head1:
        :param head2:
        :return: 若2个链表有相交节点，返回相交节点，无则返回None
        """
        if head1 is None or head2 is None:
            return

        loop1 = FindFirstIntersectNode.get_loop_node(head1)
        loop2 = FindFirstIntersectNode.get_loop_node(head2)

        if loop1 is not None and loop2 is not None:
            return FindFirstIntersectNode.both_loop(head1, loop1, head2, loop2)
        elif loop1 is None and loop2 is None:
            return FindFirstIntersectNode.no_loop(head1, head2)

    @staticmethod
    def no_loop(head1, head2):
        """
        :param head1:
        :param head2:
        :return: 两个无环链表的相交节点
        """
        if head1 is None or head1.next is None:
            return

        n = 0
        cur1 = head1
        cur2 = head2
        while cur1.next is not None:
            n = n + 1
            cur1 = cur1.next
        while cur2.next is not None:
            n = n - 1
            cur2 = cur2.next

        if cur1 != cur2:
            return None
        else:
            cur1 = head1 if n >= 0 else head2
            cur2 = head2 if cur1 == head1 else head1
            n = abs(n)

        while n > 0:
            n = n - 1
            cur1 = cur1.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    @staticmethod
    def both_loop(head1, loop1, head2, loop2):
        """
        :param head1:
        :param loop1:
        :param head2:
        :param loop2:
        :return: 两个有环链表的相交节点
        """
        if loop1 == loop2:
            n = 0
            cur1 = head1
            cur2 = head2
            while cur1.next != loop1:
                n = n + 1
                cur1 = cur1.next
            while cur2.next != loop1:
                n = n - 1
                cur2 = cur2.next

            cur1 = head1 if n >= 0 else head2
            cur2 = head2 if cur1 != head1 else head1
            n = abs(n)
            while n > 0:
                n = n - 1
                cur1 = cur1.next

            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1

        else:
            cur1 = loop1.next
            while cur1 != loop1:
                cur1 = cur1.next
                if cur1 == loop2:
                    return loop1
            return None


if __name__ == '__main__':
    lyst1 = [2, 1, 0, 4, 7, 9, 3]
    lyst2 = [8, 3, 5, 0]
    link_list1 = LinkList()
    link_list2 = LinkList()
    link_list1.create(lyst1)
    link_list2.create(lyst2)
    head1 = link_list1.get_head()
    head2 = link_list2.get_head()
    tail1 = link_list1.get(link_list1.length() - 1)
    tail2 = link_list2.get(link_list2.length() - 1)
    tail2.next = link_list1.get(4)
    # tail.next = link_list.get(3)
    # r = FindFirstIntersectNode.get_loop_node(head1)
    res = FindFirstIntersectNode.no_loop(head1, head2)
    print(res.value)
    print('===============================')
    print('both loop, no intersect')
    lyst3 = [9, 3, 6, 1, 0, 3]
    lyst4 = [8, 3, 1, 3, 0, 4]
    link_list3 = LinkList()
    link_list4 = LinkList()
    link_list3.create(lyst3)
    link_list4.create(lyst4)
    tail3 = link_list3.get(link_list3.length() - 1)
    tail4 = link_list4.get(link_list4.length() - 1)
    tail3.next = link_list3.get(3)
    tail4.next = link_list4.get(2)
    head3 = link_list3.get_head()
    head4 = link_list4.get_head()
    loop3 = FindFirstIntersectNode.get_loop_node(head3)
    loop4 = FindFirstIntersectNode.get_loop_node(head4)
    res = FindFirstIntersectNode.both_loop(head3, loop3, head4, loop4)
    print(res)
