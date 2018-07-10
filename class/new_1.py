class Person:
    def __init__(self, name):
        self.name = name
    def Greet(self):
        print('Hello', self, 'is calling the greet method of person')
    def sayHi(self):
        print('My name is {name}'.format(name = self.name))

p = Person('The Downtown Function')
p.sayHi()