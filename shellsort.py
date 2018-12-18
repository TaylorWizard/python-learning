import random

def shellSort(lyst):
    gap = len(lyst) // 2
    while gap >= 1:
        for i in range(gap, len(lyst)):
            j = i
            while j >= gap:
                if lyst[j] < lyst[j - gap]:
                    lyst[j], lyst[j - gap] = lyst[j - gap], lyst[j]
                    j -= gap
                else: break
        gap //= 2



def main(size = 30, sort = shellSort):
    lyst = []
    for i in range(size):
        lyst.append(random.randint(0, size+20))
    lyst = sorted(set(lyst), key = lyst.index)
    print('the origin list: {0}'.format(lyst))
    sort(lyst)
    print('the list sorted is: {0}'.format(lyst))

if __name__ == '__main__':
    main()
