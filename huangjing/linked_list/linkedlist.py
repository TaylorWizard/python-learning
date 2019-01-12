from link.link_list import LinkList

class LinkedList:
    @staticmethod
    def is_palindrome_3(head):
        while n1.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next
        n1.next = None
        n3 = None
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        n3 = n1
        n2 = linklist.get_head()
        while n1.next is not None and n2.next is not None:
            if n1.value != n2.value:
                break
            n1 = n1.next
            n2 = n2.next
        n1 = n3.next
        n3.next = None
        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2

list = [1, 2, 3, 2, 1]
linklist = LinkList()
linklist.create(list)
linklist.print()
n1 = linklist.get_head()
n2 = linklist.get_head()
