from link.link_list import Node, LinkList


class SmallEqualBigger:
    # need n extra space
    @staticmethod
    def list_partition_1(head, pivot):
        print('The pivot is {pivot}'.format(pivot=pivot))
        if head is None:
            return head

        lyst = []
        cur = head

        while cur is not None:
            lyst.append(cur)
            cur = cur.next

        SmallEqualBigger.arr_partition(lyst, pivot)

        i = 1
        for i in range(i, len(lyst)):
            lyst[i - 1].next = lyst[i]

        lyst[i].next = None
        return lyst[0]

    @staticmethod
    def arr_partition(node_lyst, pivot):
        small = -1
        big = len(node_lyst)
        index = 0
        while index != big:
            if node_lyst[index].value < pivot:
                small += 1
                SmallEqualBigger.swap(node_lyst, small, index)
                index += 1
            elif node_lyst[index].value == pivot:
                index += 1
            else:
                big -= 1
                SmallEqualBigger.swap(node_lyst, big, index)

    # need O(1) extra space
    @staticmethod
    def list_partition_2(head, pivot):
        sh = None  # small head
        st = None  # small tail
        eh = None  # equal head
        et = None  # equal tail
        bh = None  # big head
        bt = None  # big tail

        while head is not None:
            next = head.next
            head.next = None
            if head.value < pivot:
                if sh is None:
                    sh = head
                    st = head
                else:
                    st.next = head
                    st = head
            elif head.value == pivot:
                if eh is None:
                    eh = head
                    et = head
                else:
                    et.next = head
                    et = head
            else:
                if bh is None:
                    bh = head
                    bt = head
                else:
                    bt.next = head
                    bt = head
            head = next

        if st is not None:
            st.next = eh
            et = st if et is None else et

        # all connect
        if et is not None:
            et.next = bh

        # sh != None 返回 sh 否則看eh 是否为空, 不为空返回eh 否则返回bh
        return sh if sh is not None else eh if eh is not None else bh

    @staticmethod
    def swap(node_lyst, x, y):
        node_lyst[x], node_lyst[y] = node_lyst[y], node_lyst[x]

    @staticmethod
    def print_linked_list(node):
        print('Linked list: ', end='')
        while node is not None:
            print(node.value, end=' ')
            node = node.next


if __name__ == '__main__':
    lyst = [1, 2, 33, 4, 55, 6, 76, 6, 78]
    link_list = LinkList()
    link_list.create(lyst)
    # new_head = SmallEqualBigger.list_partition_1(link_list.head, 55)
    new_head = SmallEqualBigger.list_partition_2(link_list.head, 55)
    SmallEqualBigger.print_linked_list(new_head)
