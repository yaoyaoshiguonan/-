# a = int(input)
# if a > 5:
#     print("%d is big"%a)
#     print("%d + 1 = %d"%(a,a+1))
# else:
#     print("%d is small"%a)
#     print("%d - 1 = %d"%(a,a-1))
# print("hello world")
#练习：输入一个整数，输出这个数的绝对值
# a = int(input())
# if a < 0:
#     a = -a
# print("%d"%a)
#练习：输入两个整数，输出两个数中较大的那个
# a, b = map(int, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)
#练习：输入三个整数，输出三个数中最大的那个
# a,b,c=map(int,input(.split())
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# '''
# 练习：
# 输入一个0到100之间的分数，
# 如果大于等于85，输出A；
# 如果大于等于70并且小于85，输出B；
# 如果大于等于60并且小于70，输出C；
# 如果小于60，输出 D；
# '''
# a = int(input())
# if a >= 85:
#     print('A')
# elif a >= 70:
#     print('B')
# elif a >= 60:
#     print('C')
# else:
#     print('D')
# '''
# 练习：
#
# 1.判断闰年。闰年有两种情况：
# (1) 能被100整除时，必须能被400整除；
# (2) 不能被100整除时，被4整除即可。
# 输入一个年份，如果是闰年输出yes，否则输出no。
#
# '''
# a = int(input())
# if a % 100 == 0:
#     if a %400 == 0:
#         print('yes')
# elif a % 4 == 0:
#     print('yes')
# else:
#     print('no')
# '''
# 4. pass 语句
# pass 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句。
#
# '''
# x = int(input())
# if x > 5:
#     pass
# else:
#     print(x)
# '''
#
# 5. 变量的作用域
# if语句内部的变量，可以在语句外访问。
#
# '''
# a,b=map(int,input().split())
# if a > b:
#     max = a
# else:
#     max = b
# print(max)
# '''
#
# 二、条件表达式
# (1) 与 and
# (2) 或 or
# (3) 非 not
#
# 注意：运算符优先级：not > and > or
#
# '''
#
# #练习：用一条if语句，判断闰年
# a = int(input())
# if a%100!=0 and a%4==0 or a%400==0:
#     print('yes')
# else
#     print('no')

# '''
# 三、三元运算
# 类似于C++、Java中的问号表达式。例如：
#
# '''
# a,b=map(int,input().split())
# max = a if a>b else b
# '''
# 四、match语句
# python3.10开始新增了match语句。目前作业评测器的Python3采用旧版本，尚未支持match语法。
#
# 注意：
#
# 只有第一个匹配的模式会被执行。且跟C++、Java不同，匹配后只会执行当前模式，不会顺次执行后面的case。
# 可以用 | 表示匹配多个模式。
# 变量名 _ 被作为 通配符 并必定会匹配成功。
# 如果没有 case 匹配成功，则不会执行任何分支。
#
# '''
# status = int(input())
#
# match status:
#     case 400:
#         print("Bad request")
#     case 404:
#         print("Not found")
#     case 418 | 420 | 422:
#         print("I'm a teapot")
#     case _:
#         print("Something's wrong with the internet")
'''
注意if和else语句后一定要加冒号。
判断语句内部的代码一定要记得缩进。
格式化字符串中想表示%时，需要写%%。
Python中交换两个变量，可以用：a, b = b, a。
Python中的比较运算符支持链式操作，这一点跟C++和Java等语言不同。例如，给三个数排序的代码可以这么写：
a, b, c = map(int, input().split())
x, y, z = a, b, c

if a >= b >= c:
    print(c, b, a)
elif a >= c >= b:
    print(b, c, a)
elif b >= a >= c:
    print(c, a, b)
elif b >= c >= a:
    print(a, c, b)
elif c >= a >= b:
    print(b, a, c)
elif c >= b >= a:
    print(a, b, c)

'''
