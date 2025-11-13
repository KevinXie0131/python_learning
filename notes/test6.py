var1: int = 12
var5 = 12 # type: int
var2: float = 3.45
var3: str = 'abc'
var4: bool = True

class Student:
    pass

stu: Student = Student()

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
