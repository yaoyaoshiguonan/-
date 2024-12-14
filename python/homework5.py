#760. 字符串长度
# a = str(input())
# b = len(a)
# print(b)

# 761. 字符串中的数字个数
# a = str(input())
# b = 0
# for i in range(len(a)):
#     if "9">=a[i]>="0":
#         b+=1
# print(b)

#765. 字符串加空格
# a = str(input())
# b = " "
# print(b.join(a))

#769. 替换字符
# a =str(input())
# b =str(input())
# print(a.replace(b,"#"))

#773. 字符串插入
#
# from sys import stdin
# for line in stdin.readlines():
#     a, b = line.strip().split()# 去除每行末尾的换行符并分割字符串
#     x = max(a)# 找到字符串 a 中字典序最大的字符
#     y = a.find(x)+1
#     c = a[:y]
#     d = a[y:]
#     print(c+b+d)

#772. 只出现一次的字符
# a = str(input())
#
# x = [0 for i in range(26)]
#
# for c in a:
#     x[ord(c) - 97]+=1
# for c in a:
#     if x[ord(c) -97] == 1:
#         print(c)
#         break
# else:
#     print("no")

#764. 输出字符串
# a = input()
# c = list(a)
# for i in range(len(a)):
#     c[i] = chr(ord(a[i])+ ord(a[(i+1)%len(a)]))
# nea = ''.join(c)
# print(nea)

#771. 字符串中最长的连续出现的字符
# a = int(input())
# for i in range(a):
#     min1 = 0
#     tmp = 0
#     c = 0
#     b = input()
#     len0 = len(b)
#     for j in range(1, len0):
#         if b[j - 1] == b[j]:
#             tmp += 1
#         else:
#             tmp += 1
#             if tmp > min1:
#                 min1 = tmp
#                 c = ord(b[j - 1])
#             tmp = 0
#     if tmp > min1 and b[len0-1]==b[len0-2]:
#         min1 = tmp
#         c = ord(b[len0 - 1])
#         min1+=1
#     print("%s %d" % (chr(c), min1))

#762. 字符串匹配
# a = float(input())
# b = input()
# c = input()
# x = 0
# for i in range(len(b)):
#     if b[i]==c[i]:
#         x+=1
# if x/len(b)>= a:
#     print("yes")
# else:
#     print("no")

#768. 忽略大小写比较字符串大小
# a = input().lower()
# b = input().lower()
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("=")

# 763. 循环相克令
# T = int(input())
# for i in range(T):
#     a, b = input().split()
#     x, y = 0, 0
#     if a == "Bear":
#         x = 1
#     elif a == "Gun":
#         x = 2
#     if b == "Bear":
#         y = 1
#     elif b == "Gun":
#         y = 2
#
#     if x == y:
#         print("Tie")
#     elif x == (y + 1) % 3:
#         print("Player1")
#     else:
#         print("Player2")

#766. 去掉多余的空格
# a =input()
# b = []
# len0 = len(a)
# for i in range(len0):
#     if a[i]==' ' and a[i-1]!=' ':
#         pass
#     if a[i]==' ' and a[i+1]!=' ':
#         b.append(a[i])
#     elif a[i]==' ' and a[i+1]==' ':
#         pass
#     else:
#         b.append(a[i])
# ne=''.join(b)
# print(ne)

#767. 信息加密
# a = input()
# b=[]
# len0 = len(a)
# for i in range(len0):
#     if 'a' <= a[i] <= 'z':
#         b.append(chr((ord(a[i])-ord('a')+1)%26+ord('a')))
#     elif 'A' <= a[i] <= 'Z':
#         b.append(chr((ord(a[i]) - ord('A') + 1) % 26 + ord('A')))
#     else:
#         b.append(a[i])
# ne = ''.join(b)
# print(ne)

#770. 单词替换
# a = input()
# b = input()
# c = input()
# res = a.split(' ')
# for i in range(len(res)):
#     if res[i] == b:
#         res = c
# for i in res:
#     print(i,end=' ')

#774. 最长单词
# a = input()
# b = []
# for i in range(len(a)-1):
#     b.append(a[i])
# c = ''.join(b)
# res = c.split(' ')
# x = 0
# tmp = 0
# re = 0
# for i in range(len(res)):
#     tmp = len(res[i])
#     if tmp > x:
#         x = tmp
#         re = i
#     tmp=0
# print(res[re])

#775. 倒排单词
# a = input()
# res = a.split(' ')
# len0 = len(res)
# for i in range(len0-1,-1,-1):
#     print(res[i],end=' ')

#776. 字符串移位包含问题
a, b = input().split()
if len(a) < len(b):
    a, b = b, a

for i in range(len(a)):
    a = a[1:] + a[0]
    if a.find(b) != -1:
        print("true")
        break
else:
    print("false")