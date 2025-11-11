class Student:
    def add(self, x, y):
        print(self)
        return x + y

stu = Student()
sum = stu.add(1, 2)
print(sum)

buckets = [[] for _ in range(10)]
print(len(buckets))
print(buckets)
