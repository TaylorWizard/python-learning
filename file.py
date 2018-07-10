import os

detail = '''
if you wanna make your work also fun,
    use python!
'''

f = open('description.txt', 'w')
f.write(detail)
f.close()


f = open('description.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()
