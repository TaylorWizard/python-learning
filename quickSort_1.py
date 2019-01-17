def quickSort(lyst):
    quickSortHelper(lyst, 0, len(lyst) - 1)


def quickSortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quickSortHelper(lyst, left, pivotLocation - 1)
        quickSortHelper(lyst, pivotLocation + 1, right)


def partition(lyst, left, right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for count in range(left, right):
        if lyst[count] < pivot:
            lyst[count], lyst[boundary] = lyst[boundary], lyst[count]
            boundary += 1
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary


def main(size=20, sort=quickSort):
    lyst = [3, 5, 4, 1, 10, 2]
    # for index in range(size):
    #     lyst.append(random.randint(0, size + 10))
    print('the origin list is: {0}'.format(lyst))
    sort(lyst)
    print('the list sorted is: {0}'.format(lyst))


if __name__ == '__main__':
    main()
