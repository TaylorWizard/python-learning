def printMax(a, b):
    if a == b:
        print('{a} is equal to {b}'.format(a=a, b=b))
    elif a > b:
        print('{0} is maximum'.format(a))
    else:
        print('{0} is maximum'.format(b))

a = input('please input a: ')
b = input('please input b: ')
printMax(int(a), int(b))

