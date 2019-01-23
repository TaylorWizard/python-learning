import random


def heap_sort(lyst):
    for index in range(0, len(lyst)):
        heap_insert(lyst, index)

    size = len(lyst) - 1
    swap(lyst, 0, size)

    while size > 0:
        heapify(lyst, 0, size)
        size = size - 1
        swap(lyst, 0, size)


def heap_insert(lyst, index):
    while lyst[index] > lyst[(index - 1) // 2]:
        swap(lyst, index, (index - 1) // 2)
        index = (index - 1) // 2
        if index == 0:
            break


def heapify(lyst, index, size):
    left = 2 * index + 1

    while left < size:
        largest = left + 1 if left + 1 < size and lyst[left + 1] > lyst[left] else left
        largest = largest if lyst[largest] > lyst[index] else index

        if largest == index:
            break

        swap(lyst, largest, index)
        index = largest
        left = 2 * index + 1


def swap(lyst, x, y):
    lyst[x], lyst[y] = lyst[y], lyst[x]


if __name__ == '__main__':
    lyst = []
    for i in range(0, 20):
        lyst.append(random.randint(5, 10 * (i + 1)))
    print(lyst)
    heap_sort(lyst)
    print(lyst)
