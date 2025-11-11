#coding=utf-8

"""doc
doc1
doc2"""
import random

a = 1 # this is a
b = 'bbb'
c = "ccc"
d = '''ddd'''
e = """eeee
eee
eee"""

print(b)
print('this is', a)

'''
this is constant
'''
MY_CONSTANT = 12.34
print('MYCONSTANT is', MY_CONSTANT)

print(type(a))
print(type(c))
print(type(MY_CONSTANT))

price = 1_300_000
print('price is', price)

price1 = 3 ** 2
print('price1 is', price1)

speed_of_sound = 3.4e+2
print('speed is', speed_of_sound)
population = 7.8E9
print('population is', population)

s1 = ('你好，' 
    '尚硅谷')
print(s1)

print("b is %s, price is %i, price1 is %d, speed is %3.1f" % (b, price, price1, speed_of_sound))
price2 = 432.321
print(f"b is {b}, price is {price}, speed is {speed_of_sound}, price is {price2:.1f}")

print("escape char'acter")
print('escape char\'acter')
print('escape character: \nname\nage')
print('C:\\nice')
print('tab1\ttab2')

print('price1 is', str(price1))
print('int is', int('15'))
print('int is', int(25.12))
print('float is', float('15.61'))

print(9 / 6)
print(9 // 6)
print(9 % 6)

age = 18
age += 1
print(age)

print(5 == '5')
print(ord('a'))
print(ord('A'))
print(ord(' '))
print(chr(65))

b1 = True
b2 = 5 < 3
print(type(b1), b1)
print(type(b2), b2)
print(int(True))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(' '))

print(7 > 6 and 3 > 1)
print(7 < 6 and (3 / 0))
print(7 < 6 or 3 > 1)
print(9 > 3 or (3 / 0))
print(not 7 > 6)

print(0b11001)
print(0x1cf)
print(bin(25))
print(hex(463))
print(int('11001', 2))
print(int('1cf', 16))

print(id(b1))
print(id(b2))

print(random.randint(1, 10))

for number in range(1, 10, 2):
    print(number, end=' ')
print()
print(number)
