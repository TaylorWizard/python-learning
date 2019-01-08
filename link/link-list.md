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

##### 判断一个链表是否为回文结构

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

##### 反转单向和双向链表

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

##### 打印两个有序链表的公共部分

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

##### 将单向链表按某值划分成左边小、中间相等、右边大的形式

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