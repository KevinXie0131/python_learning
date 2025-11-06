#coding=utf-8

"""doc
doc1
doc2"""

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

print("b is %s, price is %i, price1 is %d, speed is %3.1f" % (b, price, price1, speed_of_sound))
print(f"b is {b}, price is {price}, speed is {speed_of_sound}")

print("escape char'acter")
print('escape char\'acter')
print('escape character: \nname\nage')
print('C:\\nice')

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
