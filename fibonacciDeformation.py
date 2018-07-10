def fibonacciDeformation(step):
    if step <= 0: return 0
    elif step == 1: return 1
    else: return 2 * fibonacciDeformation(step - 1)

input_step = input('please input number of step: ')

print(fibonacciDeformation(int(input_step)))