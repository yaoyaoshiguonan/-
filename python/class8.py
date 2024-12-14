'''
1. 类
类可以将变量、函数打包在一起，让代码在逻辑上更加清晰。
类名称一般采用驼峰命名法，函数一般采用下划线命名法。

类中函数的第一个参数都是self，用来调用类本身的变量和函数。
当调用类中函数的时候，第一个参数self不需要自己传递，Python会自动传递这个参数。

1.1 类的定义

'''
# class Hero:
#     hero_count = 0#在类中是共享的--类变量，用类变量时，习惯用类名来访问
#     def __init__(self,name,level=10):#构造函数
#         self.name=name#实例变量
#         self.level=level
#         print("Hero %s has been created."% name)
#         Hero.hero_count += 1
#
#     def __str__(self):
#         return "Hero：%s" %self.name
#
#     def greet(self):#问候
#         print("%s Hi"%self.name)
#
#     def move(self):#移动
#         print("%s:Move!"%self.name)
#     def get_level(self):#获取英雄的等级
#         return self.level
#     def next_level(self):
#         return self.get_level()+1
#
# zeus = Hero("Zeus")
# athena = Hero("Athena",6)
#
# zeus.greet()#自动传入宙斯
# athena.greet()
# print(zeus.name,athena.name)
# print(zeus.hero_count,athena.hero_count)
# athena.move()
# print(str(zeus))
'''

1.2 类变量和实例变量
每个类可以创建任意多实例。例如上面的Hero类，可以创建zeus和athena等实例。

类变量由所有实例共享，一般通过类名访问，例如Hero.hero_count。
实例变量与每个具体的实例绑定，一般通过具体实例来访问，例如zeus.name。

1.3 类的继承
子类可以继承父类的变量和函数。

self可以调用自身和父类中的变量和函数，
super()可以调用父类中的函数。
如果子类和父类的变量或函数重名，
优先使用子类的变量和函数。

'''
# class Hero:
#     hero_count = 0  # 类变量
#
#     def __init__(self, name, level=10):  # 构造函数
#         self.name = name
#         self.level = level
#         print("Hero %s has been created." % name)
#         Hero.hero_count += 1
#
#     def __str__(self):  # 定义str()函数的效果
#         return "Hero: %s" % self.name
#
#     def greet(self):  # 问候
#         print("%s: Hi!" % self.name)
#
#     def move(self):  # 移动
#         print("%s: Move!" % self.name)
#
#     def get_level(self):  # 获取这个英雄的等级
#         return self.level
#
#     def next_level(self):
#         return self.get_level() + 1  # 调用类中的其他函数
#
# class zeus(Hero):#基类、父类
#     hero_name = 'zeus'
#
#     def __init__(self,level):
#         super().__init__(zeus.hero_name,level)#调用父类函数
#
#     def greet(self):
#         print("%s: Hi(from child class)"%self.name)
#
#
# class athena(Hero):
#     hero_name = 'athena'
#     def __init__(self,level):
#         super().__init__(athena.hero_name,level)
#
#     def greet(self):
#         print("%s: Hi(from child class)"%self.name)
#
#
# Zeus = zeus(6)
# Athena = athena(8)
# print(Zeus.name,Athena.level,Hero.hero_count)
# print(str(Zeus),str(Athena))
# Zeus.greet()
# Athena.greet()
#

'''
2. 异常处理
当某段代码出现异常时，代码会被终止。此时如果不想让代码终止，可以用try ... except ... 语句来处理异常。

例如，将字符串转化成整数时，可能会出现异常：

'''
# s = input()
# try:
#     x = int (s)
#     print(x)
# except Exception as e:
#     print(e)
#
# x, y = map(int, input().split())
#
# try:
#     z = x / y
#     print(z)
# except Exception as e:
#     from traceback import print_exc
#     print(print_exc())#可以输出错误的详细信息
#
# print("Finished!")

'''
3. 模块
当项目的逻辑越来越复杂时，把所有代码写到一个文件中会相当不方便。

此时就可以将不同代码放到不同的模块中。所有模块通过文件夹和文件组织成树的形式。

自定义模块的每个文件夹中需要包含一个空__init__.py文件，用来让Python识别出这是一个模块。

示例：

文件结构如下所示：
'''

