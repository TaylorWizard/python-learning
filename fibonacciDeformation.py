def fibonacciDeformation(step):
    if step <= 0: return 0
    elif step == 1: return 1
    else: return 2 * fibonacciDeformation(step - 1)

def fobonacciDeformationIteration(step):
    former = 1
    target = 0
    if step <= 0: return 0
    elif step == 1: return 1
    elif step >=2:
        for i in range(2, step + 1):
            target = 2 * former
            former = target
        return target

def fibonacciIteration(step):
    former1 = 1
    former2 = 2
    target = 0
    if step <= 0: return 0
    elif step == 1: return 1
    elif step == 2: return 2
    elif step >= 3:
        for i in range(3, step+1):
            target = former1 + former2
            former1 = former2
            former2 = target
        return target



input_step = input('please input number of step: ')

print('fibonacciDeformation result is {0}'.format(fibonacciDeformation(int(input_step))))
print('fibonacciDeformationIteration result is {0}'.format(fobonacciDeformationIteration(int(input_step))))
print('fibonacciIteration result is {0}'.format(fibonacciIteration(int(input_step))))