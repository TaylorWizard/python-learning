firm = ['Zootopia', 'Avenger', 'Marvel', 'Spider Man', 'Iron Man', 'Bat Man']

firm_copy = firm

del firm[0]

print('firm is: ',firm)
print('firm_copy is: ', firm_copy)


firm_copy = firm[:]

del firm[0:2]

print('firm is: ', firm)
print('firm_copy is: ', firm_copy)
