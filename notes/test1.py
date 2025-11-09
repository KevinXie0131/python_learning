import math

age = 44
if age >= 18:
    adult = True
else:
    adult = False
print(adult)

if age >= 18 and age < 40:
    print('young')
elif 40 <= age  < 60:
    print('middle')
else:
    print('old')

n = 0;
while n < 3:
    print(f'this is {n}')
    n += 1
print(f'last is {n}')

for item in range(1, 3):
    print(f'this is {item}')
print(f'last is {item}')

for m in 'abc':
    print(f'{m}')

for row in range(1, 10):
    for colume in range(1, row + 1):
        print(f'{colume}*{row}={colume*row}', end='\t')
    print()

for day in range(1, 4):
    if day == 2:
        continue
      #  break
    print(f'day {day}')

question, answer, score = 'question 1', 'answer 2', 99
print(f'{question}, {answer}, {score}')

print(math.sqrt(3))

num1 = 0
def welcome(num):
    global num1
    num1 = 1
    print('welcome ', num)
welcome('home')
print(num1)

def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
greet(gender='male', age=11,name='zhangsan',height=155)
greet('zhangsan', 'male', height=155, age=11)

def greet1(name, /, gender, *, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
greet1('zhangsan', 'male', height=155, age=11)

def greet2(name, gender, age, height, msg='你好', welcome='welcome'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg} {welcome}')
greet2('zhangsan', 'male', 11, 155, 'hello', 'home')

def test1(*args):
    print(type(args), args, args[1])
test1(1, True,'test1',2.3)

def test2(**kwargs):
    print(type(kwargs), kwargs)
test2(name='张三', gender='男', age=18, height=172)

def test3(name, age, *data, **config):
    print(type(data), data, data[1])
    print(type(config), config)
test3('lisi', 12, 'swimming', 'hiking', height=155, weight=89)

print(type(None), None, bool(None))

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))

