# 以下这五个函数：既能定义对应的空容器，又能将【其他类型】转换为对应的数据类型

# list函数：1.定义空列表；2.将【可迭代对象】转换为列表
# res1 = list(range(8))
# res2 = list('欢迎来到尚硅谷')
# res3 = list({10, 20, 30, 40, 50})
# res4 = list({'张三': 72, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# tuple函数：1.定义空元组；2.将【可迭代对象】转换为元组
# res1 = tuple(range(8))
# res2 = tuple('欢迎来到尚硅谷')
# res3 = tuple({10, 20, 30, 40, 50})
# res4 = tuple({'张三': 72, '李四': 60, '王五': 85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# set函数：1.定义空集合；2.将【可迭代对象】转换为集合
# res1 = set(range(8))
# res2 = set('欢迎来到尚硅谷')
# res3 = set({10, 20, 30, 40, 50})
# res4 = set({'张三': 72, '李四': 60, '王五': 85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# str函数：1.定义空字符串；2.将【任意类型】转换为字符串
# res1 = str(range(8))
# res2 = str('欢迎来到尚硅谷')
# res3 = str({10, 20, 30, 40, 50})
# res4 = str({'张三': 72, '李四': 60, '王五': 85})
# res5 = str(False)
# res6 = str(None)
# res7 = str(100)
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)
# print(type(res5), res5)
# print(type(res6), res6)
# print(type(res7), res7)

# dict函数：1.定义空字典；2.将可迭代对象转换为字典
# 备注：交给dict函数的必须是键值对序列才可以，否则会报错
# res1 = dict({'张三': 72, '李四': 60, '王五': 85})
# res2 = dict([('张三', 72), ('李四', 60), ('王五', 85)])
# res3 = dict((('张三', 72), ('李四', 60), ('王五', 85)))
# res4 = dict({('张三', 72), ('李四', 60), ('王五', 85)})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 所有的数据容器，都支持成员运算符： in / not in
hobby = ['抽烟', '喝酒', '烫头']
numbes = (10, 20, 30, 40, 50)
message = 'hello,atguigu'
citys = {'北京', '天津', '上海', '重庆'}
score = {'张三': 72, '李四': 60, '王五': 85}

res1 = '抽烟' not in hobby
res2 = 10 not in numbes
res3 = 'hel' not in message
res4 = '武汉' not in citys
res5 = 60 not in score.values()
print(res1, res2, res3, res4, res5)