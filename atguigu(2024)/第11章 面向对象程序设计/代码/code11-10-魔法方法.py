class User(object):
    def __init__(self,name):  # 构造函数
        print('__init__被调用')
        self.name = name

    def __str__(self):
        print('__str__被调用')
        return '我的名字是%s'%self.name

    def __add__(self, other):
        print('__add__被调用')
        return self.name + other.name

    def __eq__(self, other):
        print('__eq__被调用')
        return self.name == other.name


mia = User('mia')
print(str(mia))
print(mia)
print(1+3)
print('hi '+'mia')
jack = User('jack')
print(mia+jack)
print(6==7)
print(mia==jack)
