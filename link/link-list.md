## 链表

#### 一. 形式

> 单，双链表结构只需要给定一个头部节点head， 就能找到剩下的节点

```java
// 单向链表
class Node<V>:
    Node value;
	Node next;


// 双向链表
class Node<v>
	Node value;
	Node next;
	Node last;
```

#### 二、重要技巧

1. 额外数据结构记录(哈希表等)
2. 快慢指针



#### 三、解题

> 实现一个单链表

```python
# link-list.py
# 打印调用方法前后的单链表的装饰器
def show(func):
    def wrapper(_self, *args):
        print('方法{func_name}调用前'.format(func_name=func.__name__))
        _self.print()
        print('方法{func_name}执行中'.format(func_name=func.__name__))
        func(_self, *args)
        print('方法{func_name}调用后'.format(func_name=func.__name__))
        _self.print()

    return wrapper

# Node类
class Node(object):
    # initialize node
    def __init__(self, value, p=None):
        self.value = value
        self.next = p

# 链表类实现
class LinkList:
    def __init__(self):
        self.head = None

    # 创建单链表
    def create(self, node_value_list):
        self.head = Node(node_value_list[0])
        p = self.head
        for value in node_value_list[1:]:
            p.next = Node(value)
            p = p.next

    # 生成单链表
    def generate(self):
        p = self.head
        while p is not None:
            yield p.value
            p = p.next

    # 打印单链表
    def print(self):
        print([value for value in self.generate()])

    # 获取link list的长度
    def length(self):
        p = self.head
        length = 0
        while p is not None:
            length += 1
            p = p.next

        return length

    # 获取单链表偏移元素返回并打印其节点值
    # 支持顺序索引和逆序索引: 0代表索引0位, -1代表倒数第一位， -2代表倒数第二位
    # 获取不存在的位返回None
    def get(self, offset):
        p = self.head
        index = 0
        length = self.length()

        # 超过链表最大长度
        if offset > length - 1:
            print('sorry, the node you want to get is not exist')
            return None

        # 如果传入负数, 与length相加比较, 小于0 则链表中不存在这个节点
        if offset < 0 and offset + length < 0:
            print('sorry, the node you want to get is not exist')
            return None

        # 如果传入负数, 与length相加比较, 大于0, 则存在这个节点, offset赋值为offset+length表示倒数第x个
        if offset < 0 and (offset + length >= 0):
            offset = offset + length

        while index < offset:
            p = p.next
            index += 1

        print('获取索引{index}的节点值为: {value}'.format(index=index, value=p.value))
        return p

    @show
    # 末尾加入
    def append(self, value):
        tail_node = self.get(self.length() - 1)
        tail_node.next = Node(value)

    @show
    # 在给定的index位置插入节点 值为value
    # 在两个节点之间才叫插入
    # 所以在末尾插入就是在索引倒数第一个和倒数第二个插入
    def insert(self, offset, value):
        length = self.length()
        node = Node(value)

        # 超过链表长度或者传入负数超出范围
        if offset > length - 1 or offset + length < 0:
            return None

        if offset < 0:
            offset = offset + length

        # 头部加入
        if offset == 0 or offset + length == 0:
            p = self.head
            self.head = node
            node.next = p
        # 在中间任一位置加入
        else:
            previous_node = self.get(offset - 1)
            current_node = self.get(offset)
            previous_node.next = node
            node.next = current_node

        print('在索引{index}插入节点值为: {value}'.format(index=offset, value=node.value))

    @show
    # 删除单链表偏移位元素并打印
    # 支持顺序索引和逆序索引：0代表索引0位，-1代表倒数第一位，-2代表倒数第二位
    # 删除不存在的位返回None
    def delete(self, offset):
        p = self.head
        length = self.length()
        index = 0

        if offset > length - 1:
            return None

        if offset < 0 and offset + length < 0:
            return None

        if offset == 0 or offset + length == 0:
            print('删除索引 {index} 的节点值为: {value}'.format(index=index, value=self.head.value))
            self.head = p.next
            return None

        if offset < 0 and (offset + length > 0):
            offset = offset + length

        while index < offset - 1:
            index += 1
            p = p.next
        print("删除索引 {index} 的节点值为: {value}".format(index=index + 1, value=p.next.value))
        p.next = p.next.next

    @show
    # 修改指定位置的值
    def modify(self, offset, value):
        self.get(offset).value = value

    # 逆向生成链表
    def reverse(self):
        # 将节点生成器转变为list，再逆序
        reverse_list = [value for value in self.generate()][::-1]
        self.head = Node(reverse_list[0])
        p = self.head
        for value in reverse_list[1:]:
            p.next = Node(value)
            p = p.next


if __name__ == '__main__':
    lyst = [1, 2, 33, 4, 55, 6, 76, 78]
    link_list = LinkList()
    link_list.create(lyst)
    link_list.delete(0)


```

#### 判断一个链表是否为回文结构

> 【题目】给定一个单链表的头节点head，请判断该链表是否为回文结构。
>
> 【例子】1->2->1，返回true; 1->2->2->1，返回true;15->6->15，返回true;
> 1->2->3，返回false。
>
> 【例子】如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)。

```python
# palindrome.py
from queue import LifoQueue
from link_list import Node, LinkList


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

    def is_palindrome_3(self, head):
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

    
```

#### 反转单向和双向链表

> 【题目】 分别实现反转单向链表和反转双向链表的函数
> 【要求】 如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)

```python
# reverse.py
# 反转链表
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
```

#### 打印两个有序链表的公共部分

> 【题目】 给定两个有序链表的头指针head1和head2，打印两个链表的公共部分。
> 【要求】 如果两个链表的长度之和为N，时间复杂度要求为O(N)，额外空间复
> 杂度要求为O(1)

```python
# paint_common_part.py
from link.link_list import LinkList, Node

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
```

#### 将单向链表按某值划分成左边小、中间相等、右边大的形式

> 【题目】给定一个单链表的头节点head，节点的值类型是整型，再给定一个整 数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的 节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点。 
>
> 【进阶】在实现原问题功能的基础上增加如下的要求 【要求】调整后所有小于pivot的节点之间的相对顺序和调整前一样 【要求】调整后所有等于pivot的节点之间的相对顺序和调整前一样 【要求】调整后所有大于pivot的节点之间的相对顺序和调整前一样 【要求】时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。 

```python
from link.link_list import Node, LinkList


class SmallEqualBigger:

    # need n extra space
    @staticmethod
    def list_partition_1(head, pivot):
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
        sH = None # small head
        sT = None # small tail
        eH = None # equal head
        eT = None # equal tail
        bH = None # big head
        bT = None # big tail

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
    new_head = SmallEqualBigger.list_partition_1(link_list.head, 55)

    SmallEqualBigger.print_linked_list(new_head)

```

#### 复制含有随机指针节点的链表

> 【题目】一种特殊的单链表节点类描述如下
>
> ```java
> class Node {    
> 	int value;
>    	Node next;
>     Node rand;
>     Node(int val) {
>         Node(int val) {
>   		value = val; 
>     }
> ```
>
> rand指针是单链表节点结构中新增的指针，rand可能指向链表中的任意一个节 点，也可能指向null。给定一个由Node节点类型组成的无环单链表的头节点 head，请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。 
>
> 【要求】时间复杂度O(N)，额外空间复杂度O(1) 

```python
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

    head.rand = head.next.next.next.next.next # 1 -> 6
    head.next.rand = head.next.next.next.next.next # 2-> 6
    head.next.next.rand = head.next.next.next.next # 3 -> 5
    head.next.next.next.rand = head.next.next # 4 -> 3
    head.next.next.next.next.rand = None # 5 -> None
    head.next.next.next.next.next.rand = head.next.next.next # 6 -> 4

    print('origin list: ')
    CopyListWithRandom.print_rand_linked_list(head)
    res1 = CopyListWithRandom.copy_list_with_rand_1(head)
    print('copy_1 list: ')
    CopyListWithRandom.print_rand_linked_list(res1)
    res2 = CopyListWithRandom.copy_list_with_rand_2(head)
    print('copy_2 list: ')
    CopyListWithRandom.print_rand_linked_list(res2)
```

#### 两个单链表相交的一系列问题

> 【题目】给定两个可能有环也可能无环的单链表，头节点head1和head2。请实
> 现一个函数，如果两个链表相交，请返回相交的 第一个节点。如果不相交，返
> 回null
> 【要求】如果两个链表长度之和为N，时间复杂度请达到O(N)，额外空间复杂度
> 请达到O(1)。

```python
# find_first_intersect_node.py

from link.link_list import LinkList


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
        elif loop_1 is not None and loop_2 is not None:  # 两个链表都有环
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
            while cur_1 != loop_1:
                n += 1
                cur_1 = cur_1.next

            while cur_2 != loop_2:
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
    list_2_tail.next = list_1.get(1)  # 链表2的尾节点指向链表1索引为2的节点, 即指向lyst_1的4
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
    list_3_tail.next = list_3.get(2)  # tail node 18 -> 16

    list_4.create(lyst_2)
    list_4_tail = list_4.get(list_4.length() - 1)
    list_4_tail.next = list_4.get(1)  # tail node 13 -> 11

    intersect_node = FindFirstIntersectNode.get_intersect_node(list_3.get_head(), list_4.get_head())
    print('两个链表都各自有环, 但不相交的情况')
    print('相交节点为: {0}'.format(intersect_node))

    print('===========================================')

    # 创建有相同环的两个链表, 并且有相同的入环节点
    list_5 = LinkList()
    list_6 = LinkList()

    list_5.create(lyst_1)
    list_5_tail = list_5.get(list_5.length() - 1)
    list_5_tail.next = list_5.get(2)  # list 5 tail node 16 -> 15

    list_6.create(lyst_2)
    list_6_tail = list_6.get(list_6.length() - 1)
    list_6_tail.next = list_5_tail.next  # list 6 tail node 13 -> list 5 node 15 with index 1
    intersect_node = FindFirstIntersectNode.get_intersect_node(list_5.get_head(), list_6.get_head())
    print('创建有相同环的两个链表, 并且有相同的入环节点的情况')
    print('相交节点为:{0} -- value为: {1}'.format(intersect_node, intersect_node.value))

    print('===========================================')

    # 创建有相同环的两个链表, 并且有不同的入环节点
    lyst_3 = [90, 96, 99, 100]
    list_7 = LinkList()
    list_8 = LinkList()
    list_loop = LinkList()

    # 将list_loop转为有环链表
    list_loop.create(lyst_3)
    list_loop_tail = list_loop.get(list_loop.length() - 1)
    list_loop_tail.next = list_loop.get(0)  # tail node 100 -> head node 90

    list_7.create(lyst_1)
    list_7_tail = list_7.get(list_7.length() - 1)
    list_7_tail.next = list_loop.get(0, True)  # 传入True代表是得到有环链表指定位置的节点

    list_8.create(lyst_2)
    list_8_tail = list_8.get(list_8.length() - 1)
    list_8_tail.next = list_loop.get(3, True)

    intersect_node = FindFirstIntersectNode.get_intersect_node(list_7.get_head(), list_8.get_head())
    print('创建有相同环的两个链表, 并且有不同的入环节点的情况')
    print('相交节点为:{0} -- value为: {1}'.format(intersect_node, intersect_node.value))


```