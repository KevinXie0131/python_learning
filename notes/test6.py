var1: int = 12
var5 = 12 # type: int
var2: float = 3.45
var3: str = 'abc'
var4: bool = True

class Student:
    pass

stu: Student = Student()
stu1: Student = Student()
print('stu is stu1: ', stu is stu1)
print('stu is Student: ', isinstance(stu, Student))
print('stu is Student: ', type(stu) == Student)

my_list1: list[int] = [1, 2, 3]
my_list2 = [1, 2, 3] # type: list[int]
my_tuple1: tuple[int, float, str] = (1, 1.2, 'str')

def my_fun():
    return 10

result = my_fun() # type: int

def func(data: str):
    return len(data)

print(func('a'))

def func1(data: list[int]) -> int:
    data.append(1)
    return len(data)

print(func1([1, 2]))


# 导入json模块
import json

json_data_string = '''
{
    "name": "Alice",
    "age": 30,
    "isStudent": false,
    "courses": [
        {"title": "History 101", "credits": 3},
        {"title": "Math 202", "credits": 4}
    ],
    "address": null
}
'''

# 通过 json.loads(data) 方法把json数据转化为了 python数据
data: dict = json.loads(json_data_string)
print(data)
print(type(data))
print(data.keys())
print(data.get('courses'))

# 通过 json.dumps(data) 方法把python数据转化为了 json数据
data = json.dumps(data)
print(data)
print(type(data))


def account_create(initial_amount=0):

    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款：+{num}， 账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款：-{num}， 账户余额：{initial_amount}")

    return atm

atm = account_create()

atm(100)
atm(200)
atm(100, deposit=False)


positive_infinity  = float('-inf')
print(positive_infinity )
print(type(positive_infinity))

print(max(1, 2))
print(min(1, 2))
