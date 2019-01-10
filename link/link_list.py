# link.py


def show(func):
    """

    打印调用方法前后的单链表的装饰器
    :param func:
    :return:
    """

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


class RandNode:
    def __init__(self, value, p=None, rand=None):
        self.value = value
        self.next = p
        self.rand = rand


# 链表类实现
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 返回头节点
    def get_head(self):
        return self.head

    # 创建单链表
    def create(self, node_value_list):
        self.head = Node(node_value_list[0])
        p = self.head
        for value in node_value_list[1:]:
            p.next = Node(value)
            p = p.next

        self.tail = p

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
    def length(self, loop=False):
        p = self.head
        length = 0
        if loop is False:
            while p is not None:
                length += 1
                p = p.next
        else:
            length += 1
            while p != self.tail:
                length += 1
                p = p.next

        return length

    def get(self, offset, loop=False):
        """

        获取单链表偏移元素返回并打印其节点值
        支持顺序索引和逆序索引: 0代表索引0位, -1代表倒数第一位， -2代表倒数第二位
        获取不存在的位返回None
        :param offset:
        :param loop:
        :return:
        """
        p = self.head
        index = 0
        length = self.length(loop)

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
    def insert(self, offset, value):
        """

        在给定的index位置插入节点 值为value
        在两个节点之间才叫插入
        所以在末尾插入就是在索引倒数第一个和倒数第二个插入
        :param offset:
        :param value:
        :return:
        """
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
    def delete(self, offset):
        """

        删除单链表偏移位元素并打印
        支持顺序索引和逆序索引：0代表索引0位，-1代表倒数第一位，-2代表倒数第二位
        删除不存在的位返回None
        :param offset:
        :return:
        """
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
