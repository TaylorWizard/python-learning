class SchoolMember:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
        print('')

    def tell(self):
        '''Tell my details'''
        print('Name: {0}, Age: {1}, Id_number: {2}'.format(self.name, self.age, self.id_number), end='')

class Teacher(SchoolMember):
    def __init__(self, name, age, id_number, salary):
        SchoolMember.__init__(self, name, age, id_number)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print(', Salary: {0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, id_number, marks):
        SchoolMember.__init__(self, name, age, id_number)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print(', Marks: {0:d}'.format(self.marks))


teacher = Teacher('Mrs Aristotle', 30, 123456, 30000)
student = Student('John han', 30, 220340, 45)

print()

members = [teacher, student]
for member in members:
    member.tell()