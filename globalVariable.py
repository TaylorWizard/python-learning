x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x is', x)

func()
print('Value of x is {x}'.format(x = x))