import numpy as np
import random as rd

def mergeSort(lyst):
    '''
    :param lyst: list being sorted
    :var copybuffer temporary space needed during merge
    :return:
    '''
    # initialize empty array
    copybuffer = np.empty(len(lyst))
    mergeSortHelper(lyst, copybuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copybuffer, low, high):
    '''
    :param lyst: list being sorted
    :param copybuffer: temporary space needed during merge
    :param low, high: bounds of sublist
    :var middle: midpoint of sublist
    :return:
    '''
    middle = (low + high) // 2
    if low < high:
        mergeSortHelper(lyst, copybuffer, low, middle)
        mergeSortHelper(lyst, copybuffer, middle + 1, high)
        merge(lyst, copybuffer, low, middle, high)

def merge(lyst, copybuffer, low, middle, high):
    '''
    :param lyst: list being sorted
    :param copybuffer: temporary space needed during merge
    :param low: beginning of first sorted list
    :param middle: ending of first sorted list
    :var middle + 1: beginning of second sorted list
    :param high: ending of second sorted list
    :return:
    '''

    list_1_index = low
    list_2_index = middle + 1

    for i in range(low, high + 1):
        if list_1_index > middle:
            # first sublist exhausted
            copybuffer[i] = lyst[list_2_index]
            list_2_index += 1
        elif list_2_index > high:
            # secound sublist exhausted
            copybuffer[i] = lyst[list_1_index]
            list_1_index += 1
        elif lyst[list_1_index] < lyst[list_2_index]:
            copybuffer[i] = lyst[list_1_index]
            list_1_index += 1
        else:
            copybuffer[i] = lyst[list_2_index]
            list_2_index += 1

    for i in range(low, high + 1):
        lyst[i] = int(copybuffer[i]) #copy sorted items back to proper position in list

def main(size = 20, sort = mergeSort):
    lyst = []
    for i in range(size):
        lyst.append(rd.randint(0, size + 10))
    print('the origin lyst is: {0}'.format(lyst))
    sort(lyst)
    print('the list sorted is: {0}'.format(lyst))

if __name__ == '__main__':
    main()