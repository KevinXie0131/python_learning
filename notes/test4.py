class Student:
    def add(self, x, y):
        print(self)
        return x + y

stu = Student()
sum = stu.add(1, 2)
print(sum)

# List Comprehensions
buckets = [[] for _ in range(10)]
print(len(buckets))
print(buckets)

def return_mulitp():
    return 1, 2.2, True, None, 'abc', [11, 22, 33]

x1, x2, x3, x4, x5, x6 = return_mulitp()
print(x1, x2, x3, x4, x5, x6)

def test_func(computer):
    print(type(computer), computer)
    result = computer(2, 3)
    return result

def computer(x, y):
    return x + y

print(test_func(computer))

print(test_func(lambda x, y: x * y))


