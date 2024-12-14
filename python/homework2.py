# #665. 倍数
# a,b=map(int,input().split())
# if a % b == 0 or b % a == 0:
#     print('Sao Multiplos')
# else:
#     print('Nao sao Multiplos')

# #660. 零食
# x,y = map(int,input().split())
# if x == 1:
#     print("Total: R$ %.2f" % (y * 4.00))
# elif x == 2:
#     print("Total: R$ %.2f" % (y * 4.50))
# elif x == 3:
#     print("Total: R$ %.2f" % (y * 5.00))
# elif x == 4:
#     print("Total: R$ %.2f" % (y * 2.00))
# else:
#     print("Total: R$ %.2f" % (y * 1.50))

# #669. 加薪
# a = float(input())
# if a <= 400.00:
#     print("Novo salario: %.2f"%(a*1.15))
#     print("Reajuste ganho: %.2f"%(0.15*a))
#     print("Em percentual: 15 %")
# elif a <=800.00:
#     print("Novo salario: %.2f" % (a * 1.12))
#     print("Reajuste ganho: %.2f" % (0.12 * a))
#     print("Em percentual: 12 %")
# elif a <=1200.00:
#     print("Novo salario: %.2f" % (a * 1.1))
#     print("Reajuste ganho: %.2f" % (0.1 * a))
#     print("Em percentual: 10 %")
# elif a <=2000.00:
#     print("Novo salario: %.2f" % (a * 1.07))
#     print("Reajuste ganho: %.2f" % (0.07 * a))
#     print("Em percentual: 7 %")
# else:
#     print("Novo salario: %.2f" % (a * 1.04))
#     print("Reajuste ganho: %.2f" % (0.04 * a))
#     print("Em percentual: 4 %")

# #671.DDD
# a = int(input())
# if a == 61:
#     print("Brasilia")
# elif a == 71:
#     print("Salvador")
# elif a== 11:
#     print("Sao Paulo")
# elif a== 21:
#     print("Rio de Janeiro")
# elif a == 32:
#     print("Juiz de Fora")
# elif a== 19:
#     print("Campinas")
# elif a == 27:
#     print("Vitoria")
# elif a == 31:
#     print("Belo Horizonte")
# else:
#     print("DDD nao cadastrado")

# #667. 游戏时间
# a,b=map(int,input().split())
# if b > a:
#     print("O JOGO DUROU %d HORA(S)"%(b - a))
# elif a >= b:
#     print("O JOGO DUROU %d HORA(S)" % (b - a + 24))

# #663. 简单排序
# a,b,c=map(int,input().split())
# x = a
# y = b
# z = c
# if a < b:
#     if a > c:
#         a,c = c,a
#     if b > c:
#         b,c = c,b
# else:
#     a,b=b,a
#     if a > c:
#         a,c = c,a
#     if  b > c:
#         b,c = c,b
#
# print(a)
# print(b)
# print(c)
# print(' ')
# print(x)
# print(y)
# print(z)

# #657. 选择练习1
# a,b,c,d=map(int,input().split())
# if b > c and d > a and c + d > a + b and c >0 and d > 0 and a % 2 == 0:
#     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")

# #664. 三角形
# a,b,c=map(float,input().split())
# if a+b>c and b+c > a and c +a >b:
#     print("Perimetro = %.1f"%(a+b+c))
# else:
#     print("Area = %.1f"%(0.5*(a+b)*c))

# #659. 区间
# a = float(input())
# if a < 0 or a > 100:
#     print("Fora de intervalo")
# elif 25>=a>=0:
#     print("Intervalo [0,25]")
# elif 25<a<=50:
#     print("Intervalo (25,50]")
# elif 50<a<=75:
#     print("Intervalo (50,75]")
# elif 75<a<=100:
#     print("Intervalo (75,100]")

# #662. 点的坐标
# a,b=map(float,input().split())
# if a == 0 and b == 0:
#     print("Origem")
# elif a > 0 and b > 0:
#     print("Q1")
# elif a < 0 and b > 0:
#     print("Q2")
# elif a < 0 and b < 0:
#     print("Q3")
# elif a > 0 and b < 0:
#     print("Q4")
# elif a == 0:
#     print("Eixo Y")
# elif b == 0:
#     print("Eixo X")

# #672. 税
# a = float(input())
# if a<=2000:
#     print("Isento")
# elif 3000>=a>2000:
#     print("R$ %.2f"%((a-2000)*0.08))
# elif 4500>=a>3000:
#     print("R$ %.2f"%((a-3000)*0.18+80))
# elif a>4500:
#     print("R$ %.2f"%((a-4500)*0.28+350))

# #668. 游戏时间2
# a,b,c,d=map(int,input().split())
# if b > d:
#     d += 60
#     c -= 1
#     if c < a:
#         c += 24
# elif a == c and b == d:
#     c+=24
# else:
#     if c < a:
#         c +=24
#
# x = c - a
# y = d - b
# print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(x,y))

# #658. 一元二次方程公式
# a,b,c=map(float,input().split())
# if (b ** 2) - 4 * a * c < 0:
#     print("Impossivel calcular")
# elif a == 0:
#     print("Impossivel calcular")
# else :
#     print("R1 = %.5f"%((-b+((b ** 2) - 4 * a * c)**0.5)*0.5*1/a))
#     print("R2 = %.5f" % ((-b - ((b ** 2) - 4 * a * c) ** 0.5) * 0.5 * 1 / a))

# #666. 三角形类型
# a, b, c = map(float, input().split())
#
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b < c:
#     b, c = c, b
#
# if a >= b + c:
#     print("NAO FORMA TRIANGULO")
# else:
#     if a * a == b * b + c * c:
#         print("TRIANGULO RETANGULO")
#     if a * a > b * b + c * c:
#         print("TRIANGULO OBTUSANGULO")
#     if a * a < b * b + c * c:
#         print("TRIANGULO ACUTANGULO")
#     if a == b == c:  # 等价于 a == b and b == c
#         print("TRIANGULO EQUILATERO")
#     elif a == b or b == c:
#         print("TRIANGULO ISOSCELES")

#661. 平均数3
a, b, c, d = map(float, input().split())
x = (a * 2 + b * 3 + c * 4 + d) / 10
print("Media: %.1f" % x)

if x >= 7:
    print("Aluno aprovado.")
elif x < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    y = float(input())
    print("Nota do exame: %.1f" % y)
    z = (x + y) / 2
    if z >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % z)

