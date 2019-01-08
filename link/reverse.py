from link.link_list import Node, LinkList


class ReversedList:
    @staticmethod
    def reverse_link_list(head):
        pre = None
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre

    @staticmethod
    def reversed_double_link_list(head):
        pre = None
        while head is not None:
            next = head.next
            head.next = pre
            head.last = next
            pre = head
            head = next

        return pre


if __name__ == '__main__':
    lyst = [34, 21, 13, 56, 36, 19]
    link_list = LinkList()
    link_list.create(lyst)
    new_head = ReversedList.reverse_link_list(link_list.head)
    while new_head is not None:
        print(new_head.value, end=' ')
        new_head = new_head.next