from link.link_list import LinkList

class FinDFirstIntersectNode:
    @staticmethod
    def get_intersect_node(head_1, head_2):
        if head_1 is None or head_2 is None:
            return None

    @staticmethod
    def get_loop_node(head):
        if head is None or head.next is None or head.next.next is None:
            return None

        n1 = head.next  # n1 -> slow
        n2 = head.next.next  # n2 -> fast

        while n1 != n2:
            if n2.next is None or n2.next.next is None:
                return None
            n2 = n2.next.next
            n1 = n1.next

        n2 = head  # n2 -> walk again from head
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1

    @staticmethod
    def no_loop(head_1, head_2):
        if head_1 is None or head_2 is None:
            return None
        cur_1 = head_1
        cur_2 = head_2
        n = 0
        while cur_1.next is not None:
            n += 1
            cur_1 = cur_1.next
        while cur_2.next is not None:
            n -= 1
            cur_2 = cur_2.next

        if cur_1 != cur_2:
            return None

        cur_1 = head_1 if n > 0 else head_2
        cur_2 = head_2 if cur_1 == head_1 else head_1

        n = abs(n)
