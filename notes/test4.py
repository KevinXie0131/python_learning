
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

f = open('notes.txt', 'r', encoding='UTF-8')
print(f, type(f))
content = f.read()
print(content)
f.close()

f = open('notes.txt', 'r', encoding='UTF-8')
print(f.readlines())
f.close()
f.close()

f = open('notes.txt', 'r', encoding='UTF-8')
print(f.readline())
f.close()

f = open('notes.txt', 'r', encoding='UTF-8')
for line in f:
    print(line, end='')
f.close()
print()

with open('notes.txt', 'r') as f:
    print( f.readlines())

try:
    a = 1 / 0
except ZeroDivisionError as e0:
    print(e0)

try:
    print(b)
except NameError as e1:
    print(e1)

try:
 #   print(b)
    1 / 0
except (ZeroDivisionError, NameError) as e2:
    print(e2)

try:
#    1 / 0
    f = open('notes1.txt', 'r', encoding='UTF-8')
    f.close()
except Exception as ex:
    print(ex)

try:
    1 / 0
except:
    print('has exception')
else:
    print('has no exception')
finally:
    print('finally')

import time
time.sleep(1)

import time as tt
tt.sleep(1)

from time import sleep
sleep(1)

from time import *
sleep(1)

from time import sleep as sl
sl(1)

import my_module1
print(my_module1.test1(3, 4))

# from my_module1 import *
# print(test1(3, 4))
# test2(3, 1) # not found

# from my_module1 import test2
# print(test2(3, 4))


# import mypackage.my_package_module1
# mypackage.my_package_module1.print_info()

# from mypackage import my_package_module1
# my_package_module1.print_info()

# from mypackage import *
# my_package_module1.print_info()
# my_package_module2.print_info2() # not found

# from mypackage.my_package_module1 import print_info
# print_info()

from mypackage.my_package_module1 import *
print_info()
print_info1()
