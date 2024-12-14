'''

一、while循环
可以简单理解为循环版的if语句。if语句是判断一次，如果条件成立，则执行后面的语句；while是每次判断，如果条件成立，则执行循环体中的语句，否则停止。

注意，类似于if语句，while语句也需要满足：

while后需要加上冒号:
while语句的代码块需要缩进统一长度，规范写法是缩进4个空格。

'''
from setuptools.command.easy_install import is_python

# i = 0
# while i <10:
#     print(i)
#     i += 1
#练习：求1~100中所有数的立方和。
# s = 0
# i = 1
# while i <= 100:
#     s += i ** 3
#     i+=1
# print(s)

#练习：求斐波那契数列的第n项。f(1) = 1, f(2) = 1, f(n) = f(n - 1) + f(n - 2)
# n = int(input())
# a,b,i = 1,1,1
# while i < n
#     a,b = b,a + b
#     i += 1
# print(a)

'''
二、for循环
for循环语句用来按顺序枚举range、字符串等数据类型中的元素。类似于while和if语句，for语句同样需要满足冒号和缩进的要求。

注意：本节课重在学习for循环，而非学习列表、元组、集合、字典等复杂数据类型，所以for语句与这些数据类型配合的使用技巧会放到下一章中展开。

1. 遍历字符串
for语句可以遍历字符串中的每个字符。

'''
# for c in 'python':
#     print(c,end=' ')
'''
2. 遍历range
range()函数可以生成等差数列，可以接收1个、2个或者3个整数参数：

接收1个整数参数时：range(x)会按顺序返回 0,1,2,3,…x−1这个数列。
接收2个整数参数时：range(x, y)会按顺序返回 x,x+1,x+2,…,y−1这个数列。
接收3个整数参数时：range(x, y, z)分为两种情况：
z > 0时，按顺序返回 x,x+z,x+2z,x+3z,……这个数列中小于 y的所有数。
z < 0时，按顺序返回 x,x+z,x+2z,x+3z,……这个数列中大于 y的所有数。

'''
# for i in range(5):
#     print(i,end='')
# print()
#
# for i in range(3,8):
#     print(i,end='')
# print()
#
# for i in range(1,10,2):
#     print(i, end='')
# print()
#
# for i in range(0,-10,-2):
#     print(i, end='')
# print()

#练习：求1∼100中所有数的立方和。
# s = 0
# for i in range(1,101):
#     s += i **3
# print(s)

#练习：求斐波那契数列的第n项。f(1) = 1, f(2) = 1, f(n) = f(n - 1) + f(n - 2)。
# n = int(input())
# a,b=1,1
# for i in range(n-1):
#     a,b = b,a+b
# print(a)

'''
三、跳转语句
1. break
可以提前从最近的一层循环中退出，一般与if语句搭配。
例题：判断一个大于1的整数是否是质数。
'''
# n = int(input())
# is_prime = True
# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False
#         break
#
# if is_prime:
#     print("yes")
# else:
#     print("no")
'''
2. continue
可以跳过当前这次迭代后面的语句，并继续下一次迭代。作用与if语句类似。
例题：求 1∼100中所有偶数的和。

'''
# s = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         continue
#     s += i
# print(s)

'''
四、循环中的else子句和pass语句
本节内容用得不多，了解即可。

1. 循环中的else子句
for或while循环可以包括else子句，会在循环结束后执行。
不过如果循环是被break结束的，那么else子句就不会执行了。
'''

# n = int(input())
#
# for x in range(2,n):
#     if n % x == 0:
#         print("%d = %d * %d"%(n,x,n//x))
#         break
# else:
#     print("%d is a prime number"%n)
'''
2. pass语句
类似于if语句，当for或者while循环里不想写任何代码时，可以写上pass语句，这个语句不执行任何动作。

'''

# for i in range(10):  # 不进行任何操作
#     pass
#
# while True:  # 死循环
#     pass
'''
五、多层循环
while和for循环内的代码块中也可以包含循环语句。

'''
#例题：将1~100打印到一个10 * 10的矩阵中：
k = 0
for i in range(0, 10):
    for j in range(0, 10):
        print(k, end=' ')
        k += 1
    print()  # 输出回车


#练习：打印 1∼100中的所有质数。
for i in range(2,101):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

