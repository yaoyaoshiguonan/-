#708. 偶数
# for i in range(3,102,2):
#     print(i-1)

#709. 奇数
# n = int(input())
# for i in range(0,n,2):
#     print(i+1)

#712. 正数
# x = 0
# for i in range(0,6):
#     n = float(input())
#     if n <= 0:
#         continue
#     x += 1
# print("%d positive numbers"%x)

# #721. 递增序列
# n = 1
# while n != 0:
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(1,n+1):
#         print(i ,end = ' ')
#     print()

#723. PUM
# u = 1
# m,n = map(int,input().split())
# for i in range(1,m+1):
#     for j in range(1,n):
#         print(u,end = ' ')
#         u+=1
#     print('PUM')
#     u+=1
