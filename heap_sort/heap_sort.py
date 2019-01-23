import random


def get_random_list(max_len, max_value):
    res = list()
    for i in range(0, max_len):
        res.append(random.randint(0, max_value))
    return res


class Heap:
    def __init__(self, queue=None, comparator=lambda x, y: x - y):
        self.__size = 0 if queue is None else len(queue) if type(queue) == list else 0
        self.__queue = [] if queue is None else queue
        self.__comparator = comparator
        self.__sift_up_all()

    def heap_sort(self):
        for i in range(0, self.__size):
            self.__heap_insert(i)

        size = self.__size - 1
        self.__swap(0, size)

        while size > 0:
            self.__heapify(0, size)
            size = size - 1
            self.__swap(0, size)

    def peek(self):
        if self.__queue:
            return self.__queue[0]
        else:
            return None

    def empty(self):
        if not self.__queue:
            return True
        else:
            return False

    def put(self, item):
        self.__sift_up(item)

    def get(self):
        return self.__sift_down()

    def size(self):
        return self.__size

    def __sift_up(self, item):
        self.__queue.append(item)
        self.__size += 1
        self.__heap_insert(self.__size - 1)

    def __sift_down(self):
        new_item = self.__queue.pop()
        self.__size = len(self.__queue)
        if self.__queue:
            return_item = self.__queue[0]
            self.__queue[0] = new_item
            self.__heapify(0, self.__size)
            return return_item
        return new_item

    def __sift_up_all(self):
        """
        初始化整个列表为一个堆结构
        :return:
        """
        for i in range(0, self.__size):
            self.__heap_insert(i)

    def __heapify(self, index, size):
        """
        如果某个位置上的数变大或变小, 范围为index - size, 重新调整成一个堆结构, 这是一个往下沉的过程
        :param index:
        :param size:
        :return:
        """
        left = index * 2 + 1
        largest = None
        while left < size:
            if left + 1 < size and self.__comparator(self.__queue[left + 1], self.__queue[left]) > 0:
                largest = left + 1
            else:
                largest = left

            largest = largest if self.__comparator(self.__queue[largest], self.__queue[index]) > 0 else index

            if largest == index:
                break

            self.__swap(largest, index)
            index = largest
            left = index * 2 + 1

    def __heap_insert(self, index):
        """
        如果某个位置上数变小或变大, 重新调整成一个堆结构, 这是一个往上冒的过程
        :param index:
        :return:
        """
        while self.__comparator(self.__queue[index], self.__queue[(index - 1) // 2]) > 0:
            self.__swap(index, (index - 1) // 2)
            index = (index - 1) // 2
            if index == 0:
                break

    def __swap(self, a, b):
        self.__queue[a], self.__queue[b] = self.__queue[b], self.__queue[a]


if __name__ == '__main__':
    for i in range(0, 20):
        l = get_random_list(20, 200)
        # print(l)
        heap = Heap(l)
        print(heap.get())
        heap.put(9999)
        print(heap.get())
        print(l)
