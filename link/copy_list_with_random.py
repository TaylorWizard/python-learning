from link.link_list import RandNode


class CopyListWithRandom:
    @staticmethod
    def copy_list_with_rand_1(_head):
        cur = _head
        node_dict = {}
        while cur is not None:
            node_dict[cur] = RandNode(cur.value)
            cur = cur.next

        cur = _head
        while cur is not None:
            node_dict[cur].next = node_dict[cur.next] if cur.next is not None else None
            # python 字典不允许读取key为None的数据
            node_dict[cur].rand = node_dict[cur.rand] if cur.rand is not None else None
            cur = cur.next
        return node_dict[_head]

    @staticmethod
    def copy_list_with_rand_2(_head):
        cur = _head

        while cur is not None:
            _next = cur.next
            cur.next = RandNode(cur.value)
            cur.next.next = _next
            cur = _next

        cur = _head

        # set copy node rand
        while cur is not None:
            _next = cur.next.next
            cur_copy = cur.next
            cur_copy.rand = cur.rand.next if cur.rand is not None else None
            cur = _next

        res = head.next
        cur = _head

        while cur is not None:
            _next = cur.next.next
            cur_copy = cur.next
            cur.next = _next
            cur_copy.next = _next.next if _next is not None else None
            cur = _next

        return res

    @staticmethod
    def print_rand_linked_list(_head):
        cur = _head
        print('order: ', end='')
        while cur is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print('\nrand:  ', end='')
        cur = _head
        while cur is not None:
            print(cur.rand.value if cur.rand is not None else '-', end=' ')
            cur = cur.next
        print()


if __name__ == '__main__':
    head = RandNode(1)
    head.next = RandNode(2)
    head.next.next = RandNode(3)
    head.next.next.next = RandNode(4)
    head.next.next.next.next = RandNode(5)
    head.next.next.next.next.next = RandNode(6)

    head.rand = head.next.next.next.next.next  # 1 -> 6
    head.next.rand = head.next.next.next.next.next  # 2-> 6
    head.next.next.rand = head.next.next.next.next  # 3 -> 5
    head.next.next.next.rand = head.next.next  # 4 -> 3
    head.next.next.next.next.rand = None  # 5 -> None
    head.next.next.next.next.next.rand = head.next.next.next  # 6 -> 4

    print('origin list: ')
    CopyListWithRandom.print_rand_linked_list(head)
    res1 = CopyListWithRandom.copy_list_with_rand_1(head)
    print('copy_1 list: ')
    CopyListWithRandom.print_rand_linked_list(res1)
    res2 = CopyListWithRandom.copy_list_with_rand_2(head)
    print('copy_2 list: ')
    CopyListWithRandom.print_rand_linked_list(res2)
