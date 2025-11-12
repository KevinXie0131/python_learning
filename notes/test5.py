class Student:
    name = None

    def add(self, x, y):
        print(self)
        return x + y

    def say(self):
        print(f'name is {self.name}')

stu = Student()
stu.name = 'jack'
sum = stu.add(1, 2)
print(sum)

print(stu.name)
stu.say()
