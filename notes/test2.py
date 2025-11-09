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
