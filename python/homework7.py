# 4317. 不同正整数的个数
# n = int(input())
# s = set(map(int,input().split()))
# s.discard(0)
# print(len(s))

# 5302. 字符串赋值
# n = int(input())
# d={}
# for i in range(n):
#     a,b=input().split()
#     b=int(b)
#     d[a]=b
#
# m=int(input())
# for i in range(m):
#     s = input()
#     print(d.get(s,-1))

# 3207. 门禁系统
# n = int(input())
# cnt = {}
# for x in map(int,input().split()):
#     if x not in cnt:
#         cnt[x] = 0
#     cnt[x] += 1
#     print(cnx[x],end=' ')

# # 3213. 数字排序
# n = int(input())
#
# cnt = {}
# for x in map(int, input().split()):
#     if x not in cnt:
#         cnt[x] = 0
#     cnt[x] += 1
#
# a = list(cnt.items())
# a.sort(key=lambda item: (-item[1], item[0]))  # 双关键字排序
#
# for k, v in a:
#     print(k, v)