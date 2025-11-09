list1 = [1, True, False, 2.2, 'abc', None, [11, 22, 33]]
print(type(list1), list1, list1[1], list1[-1], list1[-1][1])

list2 = []
list3 = list()
print(list2, list3)

list2.append(1.1)
list2.insert(1, 2.2)
list2.extend([1, 2])
print(list2)

print(list2.pop(1))
print(list2.remove(1))
print(list2)

list2.clear()
print(list2)

del list1[1]
print(list1)

list1[1] = True
print(list1)

list4 = [10, 20, 30, 50, 20, 10]
print(list4.index(20))
print(list4.count(20))

list4.reverse()
print(list4)

list4.sort(reverse=True)
print(list4)

print(len(list4))
print(max(list4))
print(max(33, 45, 12, 78, 99))
print(min(list4))
print(sum(list4))

list5 = sorted(list4, reverse=True)
print(list5)

score_list = [62, 50, 60, 48, 80, 20, 95]
index = 0
while index < len(score_list):
    print(score_list[index], end='\t')
    index += 1
print()

for item in score_list:
    print(item, end='\t')
print()

for idx in range(len(score_list)):
    print(score_list[idx], end='\t')
print()

for index, element in enumerate(score_list, start=1):
    print(index, element, end='\t')
print()

tuple1 = (1, True, False, None, 2.2, 'abc', (11, 22, 33))
print(type(tuple1), tuple1, tuple1[1])

tuple2 = ()
tuple3 = tuple()
print(tuple2, tuple3)

tuple5 = ('a',)
print(type(tuple5), tuple5)

tuple6 = (1, True, False, None, 2.2, 'abc', [11, 22, 33])
tuple6[6][1] = 222
print(tuple6)
print(tuple6.index(2.2))
print(tuple6.count(2.2))

t1 = (23, 11, 32, 30, 17)
print(len(t1))
print(max(t1))
print(min(t1))
print(sum(t1))
t2 = sorted(t1, reverse=True)
print(t2)

index = 0
while index < len(t2):
    print(t2[index], end='\t')
    index += 1
print()

for i in t2:
    print(i, end='\t')
print()

def test(*args):
    print(f'我是test函数，我收到的参数是：{args}，参数类型是：{type(args)}')
list1 = [100, 200, 300, 400, 300]
tuple1 = ('你好', '北京', '尚硅谷', '北京')
test(list1)
test(tuple1)
test(*list1)
test(*tuple1)

msg = 'welcome@to@atguigu'
print(msg[1])
print(msg[-1])
print(msg.index('l'))
print(msg.split('@'))
print(msg.replace('@', '%'))
print(msg.count('@'))

msg = '34215尚12硅34谷4132'
print(msg.strip('2345'))
msg = ' 尚硅谷 '
print(msg.strip(' '))

print(len(msg))

msg = 'welcome to atguigu'
index = 0
while index < len(msg):
    print(msg[index], end=' ')
    index += 1
print()

for item in msg:
    print(item, end=' ')
print()

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1[::])
print(list1[0:8:2])
print(list1[8:0:-2])
print(list1[::-1])
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(tuple1[0:5:2])
print(msg[0:5:2])

list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
print(list1 + list2)
tuple1 = (10, 20, 30, 40)
tuple2 = (50, 60, 70, 80)
print(tuple1 + tuple2)
str1 = 'hello'
str2 = 'atguigu'
print(str1 + str2)

print(list1 * 2)
print(tuple1 * 2)
print(str1 * 2)

