class Student(object):
    name = None

    def __init__(self):
        print('create stu')

    def __init__(self, name):
        print('create stu with name')
        self.name = name

    def __str__(self):
        return 'this is str - ' + self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return len(self.name) <= len(other.name)

    def add(self, x, y):
        print(self)
        return x + y

    def say(self):
        print(f'name is {self.name}')

    def say2(self, message):
        print(f'name is {self.name}: {message}')

    __score = 1

    def __add_score(self):
        self.__score += 1

    def set_score(self):
        return self.__add_score()

    def get_score(self):
        return self.__score

stu = Student('')
stu.name = 'jack'
sum = stu.add(1, 2)
print(sum)

print(stu.name)
stu.say()
stu.say2('hello')


stu1 = Student('tom')
print(stu1.name)

print(stu1)
print(str(stu1))

stu2 = Student('to')
print(stu1 == stu2)

print(stu1 < stu2)
print(stu1 > stu2)

print(stu1 <= stu2)

stu.set_score()
print(stu.get_score())


class Young_Student(Student):
    age = None

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

youngStu = Young_Student( 'wang')
youngStu.setAge(12);
print(youngStu.name)
print(youngStu.getAge())
youngStu.say2('welcome')


class Old_Student(Student):
    pass

oldStu = Old_Student( 'zhang')
oldStu.say2('hi')


class Parent:
    name = 'itcast'

    def get_name(self):
        return self.name + " hello"

class Child(Parent):
    age = 11

    def get_name(self):
        # return super().get_name() + " welcome " + super().name
        return Parent.get_name(self) + " welcome " + Parent.name

child = Child()
print(child.get_name())
