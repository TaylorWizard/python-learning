car = {
    'type': 'carriage',
    'brand': 'Mercedes-Benz',
    'version': 'S600',
    'production_date': '2016-12'
}
a = [1,2,3]

input = input('please type something: ')
input = int(input, 10)
print('{0}'.format(a[input]))

print('car info: ')

for key, value in car.items():
    print('{0} is {1}'.format(key, value))

car['length'] = '4m'

if 'length' in car:
    print('length of car is: ', car['length'])

del car['length']

print(car)