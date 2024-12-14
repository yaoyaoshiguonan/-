'''
1. 元组
元组跟列表类似，只是不支持动态添加、删除元素，以及不能修改元素。

1.1 元组的初始化
元组需要用小括号括起来，中间的元素用逗号隔开。
注意，如果初始化只包含一个元素的元组，需要在该元素后添加逗号。

'''
# a=()
# b = (1,2)
# c = 6,"python",3.14
'''
1.2 元组的解包
t = 12345, 54321, "Hello!"  # 初始化一个元组
x, y, z = t  # 将元组解包，将元组内的三个值按顺序赋值给x、y、z
print(x, y, z)
所以，2. 判断语句中学习的交换操作，本质上是元组的解包：

a, b = 3, 4  # 将元组(3, 4)解包，分别赋值给a、b
a, b = b, a  # 将元组(b, a)解包，分别赋值给a、b
同样地，6. 函数中函数返回多个值，本质上也是返回了一个元组：
'''
# def calc(x, y):
#     return x + y, x * y  # 等价于 return (x + y, x * y)
#
#
# x, y = 3, 4
# s, p = calc(x, y)  # 将(x + y, x * y)解包，分别赋值给s、p
# print(s, p)
'''
1.3 元组的比较运算
元组和列表均支持比较运算符：==、!=、>、<、>=、<=等，按字典序进行比较。

1.4 元组的其他操作
元组的下标访问元素、循环遍历、切片、加法和乘法运算等操作，都与列表相同。
'''
'''
2. 集合
集合是Python中最常用的数据结构之一，用来存储不同元素。
注意，集合中的元素是无序的。

2.1 集合的初始化
创建集合用花括号或set()函数。注意：创建空集合只能用set()，不能用{}，因为{}创建的是空字典，会在下一小节里介绍字典。

集合常见的初始化方式：

# '''
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # 会自动去除重复元素
# print(basket)  # 重复的元素已经去除了
#
# s = set()  # 初始化一个空列表
# print(s)
#
# a = [1, 2, 1, 3, 1]
# b = set(a)  # 将列表转化成集合，一般是为了去重。
# c = list(b)  # 将集合转化回列表
# print(b, c)
#
# x = "abracadabra"
# a = set(x)  # 将字符串中的每个字符存到集合中
# b = str(a)  # 注意，这里并不能将集合转化回原字符串，而是用格式化表示集合中的内容
# print(a, b)

'''
2.2 集合的常用操作
假设a表示一个集合。

len(a) 返回集合中包含的元素数量。
a.add(x) 在集合中添加一个元素。
a.remove(x) 删除集合中的x，如果x不存在，则报异常。
a.discard(x) 删除集合中的x，如果x不存在，则不进行任何操作。
x in a 判断x是否在a中。
x not in a 判断x是否不在a中。
例如：
'''
# a = {1, 2, 3}
#
# print(len(a))  # 输出3
#
# a.add(4)
# print(a)  # 输出 {1, 2, 3, 4}，注意集合中的元素是无序的。
#
# a.remove(2)
# print(a)  # 输出 {1, 3, 4}
#
# #  a.remove(5)  # 因为5不存在，所以会报异常
# a.discard(5)  # 因为5不存在，所以不进行任何操作
# print(a)  # {1, 3, 4}
'''
2.3 使用for循环遍历集合
类似于列表，集合也可以用for ... in ...的形式遍历。例如：
'''
# a = {1, 2, 3}
#
# for x in a:  # 循环遍历整个集合
#     print(x, end=' ')
'''
3. 字典
字典是Python中最常用的数据结构之一，用来存储映射关系。
注意，字典中的元素是无序的。
不同于列表，字典是以key进行索引的，可以将每个key映射到某个value。
key可以是任何不可变类型，常用可以作为key的类型有数字和字符串。
列表因为是可变的，所以不能作为key。value可以是任意类型。
3.1 字典的初始化
创建字典用花括号或dict()函数。

'''
tel = {'jack': 4098, 'sape': 4139}  # 创建一个字典
print(tel)  # 输出 {'jack': 4098, 'sape': 4139}

a = dict()  # 创建一个空字典
a[123] = "abc"  # 在字典中插入一个key-value对
a[456] = "def"  # 在字典中插入一个key-value对
print(a)  # 输出 {123: 'abc', 456: 'def'}

b = list(a)  # 将字典的关键字转化成列表
print(b)  # 输出[123, 456]
'''
3.2 字典的常用操作
假设a表示一个字典。

len(a)：返回字典中的元素对数。
a[x]：获取关键字x对应的值，如果x不存在，会报异常。
a.get(x)：获取关键字x对应的值，如果x不存在，会返回None，不会报异常。
a.get(x, y)：获取关键字x对应的值，如果x不存在，会返回默认值y，不会报异常。
a[x] = y：在字典中插入一对元素，如果关键字x已存在，则将它之前映射的值覆盖掉。
del a[x]：删除关键字x对应的元素对，如果x不存在，会报异常。
x in a：检查字典中是否存在关键字x。
x not in a：检查字典中是否不存在关键字x。
a.keys()：返回字典的所有key。
a.values()：返回字典的所有value。
a.items()：返回字典的所有由key和value组成的元组。
例如：
'''
a = {'abc': 1, 'def': 2, 'python': 3}  # 初始化一个字典

print(len(a))  # 输出3
print(a['def'])  # 输出2
print(a.get('def'))  # 输出2
print(a.get('xyz', 5))  # 因为'xyz'不存在，所以输出默认值5

a['hello'] = 4  # 插入一对元素 'hello' -> 4
print(a)  # 输出{'abc': 1, 'def': 2, 'python': 3, 'hello': 4}

a['def'] = 5  # 更新'def'映射的值
print(a['def'])  # 输出5

del a['python']  # 删除关键字'python'
print(a)  # 输出{'abc': 1, 'def': 5, 'hello': 4}

print('hello' in a)  # 输出True
print(a.keys())  # 输出dict_keys(['abc', 'def', 'hello'])
print(a.values())  # 输出dict_values([1, 5, 4])
print(a.items())  # 输出dict_items([('abc', 1), ('def', 5), ('hello', 4)])
'''
3.3 使用for循环遍历字典
类似于列表，字典也可以用for ... in ...的形式遍历。例如：
'''
a = {'abc': 1, 'def': 2, 'python': 3}  # 初始化一个字典

for k in a:  # 遍历key
    print(k, end=' ')
print()  # 输出回车

for k in a.keys():  # 遍历key
    print(k, end=' ')
print()  # 输出回车

for v in a.values():  # 遍历value
    print(v, end=' ')
print()  # 输出回车

for k, v in a.items():  # 遍历key-value对
    print("(%s, %d) " % (k, v), end=' ')
print()  # 输出回车
'''
4. 作业题扩展内容
map()也可以用for ... in ...的形式遍历。
例如：for x in map(int, input().split())可以遍历一行内用空格隔开的每个整数。
map()函数的返回值也可以直接转化成set()，
例如：set(map(int, input().split()))可以将一行用空格隔开的整数存到set()中。
sorted()函数可以将列表、元组、集合、字典排序，并返回一个新列表。
如果对字典排序，则返回字典所有key排序后的列表。
'''