from link.link_list import Node, LinkList

class FindFirstIntersectNode:
    @staticmethod
    def get_intersect_node(head_1, head_2):
        """

        :param head_1: 第一个链表的头节点
        :param head_2: 第二个链表的头节点
        :return: 返回相交节点
        """
        if head_1 is None or head_2 is None:
            return None

        loop_1 = FindFirstIntersectNode.get_loop_node(head_1)
        loop_2 = FindFirstIntersectNode.get_loop_node(head_2)

        # 不会出现一个链表有环, 一个链表没有环的情况, 因为每个节点只有一个next指针

        # 当两个链表都没有环
        if loop_1 is None and loop_2 is None:
            return FindFirstIntersectNode.no_loop(head_1, head_2)
        elif loop_1 is not None and loop_2 is not None: # 两个链表都有环
            return FindFirstIntersectNode.both_loop(head_1, loop_1, head_2, loop_2)

    @staticmethod
    def get_loop_node(head):
        """

        get loop node of linked list
        :param head:
        :return:

        1、创建一个慢指针，一个快指针, 慢指针一次走一步, 快指针一次走两步
        2、快、慢指针同时走，第一次相遇后, 快指针回到开头, 慢指针停在原地不动
        3、这时快指针改为走一步, 快、慢指针再次同时一起走
        4、再次相遇一定就是入环的节点(这是结论, 想知道证明请自行查阅相关资料)
        """
        if head is None or head.next is None or head.next.next is None:
            return None

        n1 = head.next  # n1 -> slow
        n2 = head.next.next  # n2 -> fast

        # 快、慢指针第一次同时走, 相遇就跳出
        while n1 != n2:
            if n2.next is None or n2.next.next is None:
                return None
            n2 = n2.next.next
            n1 = n1.next

        # 此时快指针改为走一步
        n2 = head  # n2 -> walk again from head

        # 两个指针再次同时走, 再次相遇的节点就是入环节点
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1

    @staticmethod
    def no_loop(head_1, head_2):
        """

        两个无环链表找到第一个相交节点
        :param head_1: 第一个链表的头节点
        :param head_2:  第十个链表的头节点
        :return: 返回第一个相交的节点

        1、先判断哪个链表的长度更长, 分别统计两个链表的长度, 得到与短的链表的长度差 n
        2、长链表先走 n 步
        3、然后长链表的指针原地不动开始走, 短链表从头和长链表一起走
        4、找到的第一个两个链表相待的节点, 就是要找的第一个相交节点
        """
        if head_1 is None or head_2 is None:
            return None
        cur_1 = head_1
        cur_2 = head_2
        n = 0
        # 得到第一个链表的长度
        while cur_1.next is not None:
            n += 1
            cur_1 = cur_1.next
        # 得到第二个链表的长度
        while cur_2.next is not None:
            n -= 1
            cur_2 = cur_2.next

        # 如果两个链表的最后一个节点不相等, 那么一定不相交
        if cur_1 != cur_2:
            return None

        cur_1 = head_1 if n > 0 else head_2 # 谁的长度更长, 就赋值给cur_1
        cur_2 = head_2 if cur_1 == head_1 else head_1 # 谁的长度更短, 就赋值给cur_2

        n = abs(n)

        # 先让长的链表先走两个链表长度差 n 的 步数
        while n != 0:
            n -= 1
            cur_1 = cur_1.next

        # 这时两个链表一起走, 如果第一次发现两个节点相等, 就跳出while, 这个节点就是相交的第一个节点
        while cur_1 != cur_2:
            cur_1 = cur_1.next
            cur_2 = cur_2.next

        return cur_1


    @staticmethod
    def both_loop(head_1, loop_1, head_2, loop_2):
        """
        :param head_1: 第一个链表的头节点
        :param loop_1: 第一个链表的入环节点
        :param head_2: 第二个链表的头节点
        :param loop_2: 第二个链表的入环节点
        :return:
        """
        # 如果两个链表的入环节点相等, 以两个链表都是无环的情况找到第一个相交节点
        # 详细看no_loop函数
        if loop_1 == loop_2:
            cur_1 = head_1
            cur_2 = head_2

            n = 0
            while cur_1 is not None:
                n += 1
                cur_1 = cur_1.next

            while cur_2 is not None:
                n -= 1
                cur_2 = cur_2.next

            cur_1 = head_1 if n > 0 else head_2
            cur_2 = head_2 if cur_1 == head_1 else head_1

            n = abs(n)

            while n != 0:
                n -= 1
                cur_1 = cur_1.next

            while cur_1 != cur_2:
                cur_1 = cur_1.next
                cur_2 = cur_2.next

            return cur_1
        else:
            cur_1 = loop_1.next
            while cur_1 != loop_1:
                if cur_1 == loop_2:
                    return loop_1
                cur_1 = cur_1.next
            return None

if __name__ == '__main__':
    lyst_1 = [1, 4, 15, 16]
    lyst_2 = [10, 11, 12, 13]

    # 创建两个无环链表
    list_1 = LinkList()
    list_1.create(lyst_1)

    list_2 = LinkList()
    list_2.create(lyst_2)
    list_2_tail = list_2.get(list_2.length() - 1)
    list_2_tail.next = list_1.get(1) # 链表2的尾节点指向链表1索引为2的节点, 即指向lyst_1的4
    intersect_node = FindFirstIntersectNode.get_intersect_node(list_1.get_head(), list_2.get_head())
    print('相交节点为:{0} -- value为: {1}'.format(intersect_node, intersect_node.value))
    print('list 1: ', end='')
    list_1.print()
    print('list 2: ', end='')
    list_2.print()

    print('===========================================')

    # 创建两个有环链表, 但不相交
    list_3 = LinkList()
    list_4 = LinkList()

    list_3.create(lyst_1)
    # 得到list_3的最后一个节点
    list_3_tail = list_3.get(list_3.length() - 1)
    list_3_tail.next = list_3.get(2) # tail node 18 -> 16

    list_4.create(lyst_2)
    list_4_tail = list_4.get(list_4.length() - 1)
    list_4_tail.next = list_4.get(1) # tail node 13 -> 11

    intersect_node = FindFirstIntersectNode.get_intersect_node(list_3.get_head(), list_4.get_head())
    print('两个链表都各自有环, 但不相交的情况')
    print('相交节点为: {0}'.format(intersect_node))

    print('===========================================')

    # 创建有相同环的两个链表, 并且有相同的入环节点
    list_5 = LinkList()
    list_6 = LinkList()

    list_5.create(lyst_1)
    list_5_tail = list_5.get(list_5.length() - 1)
    list_5_tail.next = list_5.get(1) # list 5 tail node 16 -> 4

    list_6.create(lyst_2)
    list_6_tail = list_6.get(list_6.length() - 1)
    list_6_tail.next = list_5_tail.next # list 6 tail node 13 -> list 5 node 4 with index 1
    # print('创建有相同环的两个链表, 并且有相同的入环节点', list_6.get_head().value)                          s

    # intersect_node = FindFirstIntersectNode.get_intersect_node(list_5.get_head(), list_6.get_head())

    # 创建有相同环的两个链表, 并且有不同的入环节点