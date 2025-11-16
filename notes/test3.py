set1 = {0, 1, True, False, None, 2.3, 2.3, 'abc', 'abc', (11, 22, 33), (11, 22, 33)}
print(type(set1), set1)

set2 = set()
print(type(set2), set2)

set3 = frozenset([0, 1, True, False, None, 2.3, 2.3, 'abc', 'abc', (11, 22, 33), (11, 22, 33)])
set4 = frozenset({0, 1, True, False, None, 2.3, 2.3, 'abc', 'abc', (11, 22, 33), (11, 22, 33)})
print(type(set3), set3)
print(type(set4), set4)

set5 = frozenset()
print(type(set5), set5)

set1.add(12.34)
print(set1)
set1.update([31, 32])
print(set1)
set1.update({33})
print(set1)
set1.update((34, ))
print(set1)
set1.remove(34)
print(set1)
set1.discard(33)
print(set1)
print(set1.pop())
print(set1.pop())
set1.clear()
print(set1)

s1 = {10, 20, 30, 40, 50}
s1.remove(20)
s1.add(60)
print(s1)

print(10 in s1)
print(110 not in s1)

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

print(s1.union(s2))

s3 = {30, 40, 50}
print(s3.issubset(s2))
print(s2.issuperset(s3))
print(s2.isdisjoint(s1))

s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}
print( s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

for item in s1:
    print(item, end=' ')
print()

for item in frozenset(s1):
    print(item, end=' ')
print()

dict1 = {'zhangsan': 11, 20254144: True, 'wangwu': 22.3, 'zhaoliu': None, 'jack': {1,2}, 'tom': [12.3, 32.4], 'rose': ('abc',), 'mary': 'A1B2C3', 'mary': 'A1b2C3'}
print(type(dict1), dict1)
d1 = {}
d2 = dict()
print(type(d1), d1)
print(type(d2), d2)

print(dict1['zhangsan'])
dict1['zhangsan'] = [11, 22]
print(dict1['zhangsan'])

del dict1['zhangsan']
print(dict1)

print(dict1.pop(20254144))
print(dict1)
print(dict1.pop(20254145, 'not found'))

dict1.clear()
print(dict1)

dict1['a1'] = 1.23
print(dict1)
dict1.update({'b2': True, 'c3': '123'})
print(dict1)

print(dict1.get('d4', 'Not Found'))

print(type(dict1.keys()), dict1.keys())
for key in dict1.keys():
    print(key, dict1[key], end='->')
print()

print(type(list(dict1.keys())), list(dict1.keys()))

print(type(dict1.values()), dict1.values())
for v in dict1.values():
    print(v, end=' ')
print()

print(type(list(dict1.values())), list(dict1.values()))

print(type(list(dict1.items())), list(dict1.items()))
for i in dict1.items():
    print(type(i), i, i[0], i[1], end=' ')
print()

d1 = {'张三': 72, '李四': 60, '王五': 85}
for key in d1:
    print(f'{key}的成绩是{d1[key]}')
    
for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')

print('李四' in d1.keys())
print(60 in d1.values())
print(61 not in d1.values())
