# 由于是有序链表，所以就不需要一遍遍地去搜索链表中的每个值的大小，
# 如果遇到无序链表，第一件事还是要先排序，毕竟排序的时间复杂度可
# 以做到O(NlogN)，而一遍遍的搜索的话，复杂度一定是O(N^2)。

from link.link_list import LinkList


def print_common_part(head_1, head_2):
    print('Common part: ')
    # 使用外排法, 在归并排序使用过
    while head_1 is not None and head_2 is not None:
        if head_1.value < head_2.value:
            head_1 = head_1.next
        elif head_1.value > head_2.value:
            head_2 = head_2.next
        else :
            print(head_1.value, end=' ')
            head_1 = head_1.next
            head_2 = head_2.next


if __name__ == '__main__':
    lyst_1 = [2, 3, 5, 6]
    lyst_2 = [1, 3, 5, 6, 7, 8]

    link_list_1 = LinkList()
    link_list_1.create(lyst_1)
    link_list_2 = LinkList()
    link_list_2.create(lyst_2)
    print_common_part(link_list_1.head, link_list_2.head)

