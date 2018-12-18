from time import sleep
f = open('description.txt', 'r')
try:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sleep(2)
except KeyboardInterrupt:
    print('You cancelled the reading from the file.')
finally:
    f.close()
    print('\n(Cleaning up: closed the file)')
