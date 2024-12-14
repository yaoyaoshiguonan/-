# #804. n的阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# n = int(input())
# res = fact(n)
# print(res)

#805. x和y的最大值
# def max(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# x,y=map(int,input().split())
# print(max(x,y))

# 808. 最大公约数
# def gcd(a,b):
#     if a < b:
#         a,b=b,a
#     a = a - b
#     if a!=b:
#         return gcd(a,b)
#     else:
#         return a
# a,b=map(int,input().split())
# print(gcd(a,b))

#812. 打印数字
# def print1D(a,size):
#     for i in range(size):
#         print(a[i],end=' ')
# b,c=map(int,input().split())
# a = list(map(int, input().split()))
# print1D(a,c)

#816. 数组翻转
# def reserve(a,b):
#     for i in range(b//2):
#         a[i],a[b-1-i]=a[b-1-i],a[i]
# c,b=map(int,input().split())
# a = list(map(int,input().split()))
# reserve(a,b)
# for i in range(c):
#     print(a[i],end=' ')

# 820. 递归求斐波那契数列
# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# n = int(input())
# x = f(n)
# print(x)

#810. 绝对值
# n = int(input())
# n = abs(n)
# print(n)

# 806. 两个数的和
# def add(x, y):
#     return x + y
#
#
# x, y = map(float, input().split())
# print("%.2f" % add(x, y))

# 807. 区间求和
#
# def sum(l, r):
#     res = 0
#     for i in range(l, r + 1):
#         res += i
#     return res
#
#
# l, r = map(int, input().split())
# print(sum(l, r))

# 809. 最小公倍数
# def gcd(a,b):
#     if a < b:
#         a,b=b,a
#     a = a - b
#     if a!=b:
#         return gcd(a,b)
#     else:
#         return a
# a,b=map(int,input().split())
# print(a*b//gcd(a,b))
#两个数的乘积等于这两个数的最大公约数与最小公倍数的积。

