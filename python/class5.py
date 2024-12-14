'''
1. 字符与整数的联系——ASCII码
每个常用字符都对应一个-128 ~ 127的数字，二者之间可以相互转化。注意：目前负数没有与之对应的字符。

ord()函数可以求一个字符的ASCII码。注意输入是一个字符，而不是字符串。
chr()函数可以将一个ASCII码转化成对应的字符。

'''
# c = 'a'
# print(ord(c))
#
# a = 66
# print(chr(a))

'''
常用ASCII值：'A'- 'Z'是65 ~ 90，'a' - 'z'是97 - 122，0 - 9是 48 - 57。

注意：虽然字符可以跟整数相互转化，
但在Python中，字符不能参与数值运算，这一点跟C++、Java等语言是不同的。

2. 字符串常量的写法
在Python中，字符串既可以用单引号来表示，也可以用双引号来表示，二者完全相同。
这一点跟C++、Java等编程语言是不同的，
在这些编程语言中，用单引号来表示字符，用双引号来表示字符串。
'''
# a = 'hello world'
# print(a)
#
# b = "hello wrold"
# print(b)
# #两个或多个字符串常量并排写，会被自动合并，例如：
# a = "MY" "name ""is yxc"
'''
一个字符串如果包含多行，
可以采用"""..."""或者'''    '''的初始化方式，字符串中将自动包含回车字符，例如：

'''
# a = """Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to"""
# print(a)

'''
3. 表示特殊字符——转义
当想在字符串中表示特殊字符时，一般可以在字符前加反斜杠\。常见需要转义的字符有：

转义字符	含义	ASCII码（十进制）
\n	回车	10
\\	代表一个反斜杠\	92
\"	表示一个双引号	34
\'	表示一个单引号	39

'''
# print("My name is:\n\"yxc!\"")

#另外，如果想输出单引号，也可以用双引号来表示，反之亦然。例如
# print("My name is 'yxc!'")  # 输出：My name is 'yxc!'
# print('My name is "yxc!"')  # 输出：My name is "yxc!"
'''
4. 访问字符串中的每个字符
可以通过下标读取字符串中的每个字符，下标从0开始，也可以是负数，负数下标表示的是除以字符串长度的余数对应的位置。

负数下标相当于将字符串首位相接，然后从0往前数。
如果字符串长度是 n，那么下标只能取 −n∼n−1之间的整数，超出范围会报错。

注意：字符串中的每个字符不能修改。
'''
# a = "hello world"
# print(a[0],ord(a[5]))
#a[2] = 'x'  # 会报错，字符串不能修改
'''
5. 使用循环语句遍历字符串
可以通过下标访问，例如：
'''
# s = "acwing"
# for i in range(6):
#     print(s[i],end=' ')
# print()
# #可以通过for ... in ...直接遍历，例如：
# for c in "python":
#     print(c, end=' ')  # 注意c本身也是字符串类型
# print()  # 输出回车
'''
6. 字符串的切片操作
字符串的切片操作会返回一个新字符串。用法：

a[begin:end] 会返回包含a[begin], a[begin + 1], ..., a[end - 1]的字符串。
省略begin时，begin的默认值是0。
省略end时，end的默认值是字符串长度。
如果begin或end是负数，表示的是除以字符串长度后的余数。
例如：
'''

# a = "ABCDE"
# print(a[1:4])  # 输出BCD
# print(a[1:])  # 输出BCDE
# print(a[:4])  # 输出ABCD
# print(a[:])  # 输出ABCDE
# print(a[-4:-1])  # 等价于print(a[1:4])
#注意：字符串的切片不支持写操作。
'''
例如：

a = "ABCDE"
a[1:4] = "XY"  # 会报错，字符串不能修改

7. 字符串的复制
跟列表不同，字符串的每次复制操作，都会得到一个全新的字符串。

8. 字符串的运算
字符串的加法可以将两个字符串拼接起来，得到一个新字符串。
字符串乘以一个整数，可以将若干个自身拼接起来，得到一个新字符串。
字符串支持比较运算符，按字典序比较大小。即如果两个字符串相同，则表示相等；
否则找到两个字符串从左到右数第一个不一样的字符，哪个字符串的字符的ASCII码小，
哪个字符串的字典序就小；另外空字符比任何字符都小。
例如：
'''
# a = "Hello "
# b = "World"
# c = a + b
# print(c)  # 输出Hello World
#
# d = a * 3
# print(d)  # 输出Hello Hello Hello
#
# e = a * 3 + "World"
# print(e)  # 输出Hello Hello Hello World
#
# print(a <= b)  # 按字典序比较大小，输出True
# print("123" > "22")  # 按字典序比较大小，输出False

'''
9. 字符串的常用操作
假设s是一个字符串，则：

len(s)返回字符串长度。
s.split(sep)返回一个字符串列表。如果给出了sep就按sep分隔；如果没给出，则会按空格分隔，但连续的空格会被视为单个分隔符，而且会忽略首尾的空白字符。
s.strip()将首尾的空白字符删除。
s.replace(old, new)将s中所有的old子串都改成new。
s.find("abc")查询某个子串在s中第一次出现的下标；如果不存在，则返回-1。
s.startswith(prefix)判断prefix是否为s的前缀。
s.endswith(suffix)判断suffix是否为s的后缀。
s.lower()将所有大写字母变成小写。
s.upper()将所有小写字母变成大写。
s.join(a)，a是一个字符串列表，这个函数返回将a中的字符用s作为分隔符拼接起来的结果。
注意：返回的所有字符串都是新字符串，原字符串不变。

例如：
'''
s1 = "abc def xyz"
print(len(s1))
print(s1.split())

s2 = "  abc abc  "
print(s2.strip())
print(s2.replace("abc","*"))
print(s2.find("abc"),s2.find("xxx"))
s3="Abc deF"
print(s3.startswith("Ab"))
print(s3.endswith("eF"))
print(s3.lower())
print(s3.upper())
s4=","
a=["aa","bb","cc"]
print(s4.join(a))
'''
10. 更复杂的格式化输出
当需要用到更复杂的格式化输出时，现查即可。可以参考：

更复杂的输出格式
printf 风格的字符串格式化

11. 作业题扩展内容
作业的评测器会自动忽略每一行的行末空格，所以行末输出多余空格也视为正确。
s.isdigit()：当字符串s不是空字符串，且包含的所有字符都是数字时返回True，否则返回False。
a, b = ["abc", "def"]这种写法可以将"abc"赋值给第一个变量a，将"def"赋值给第二个变量b。
s.rfind("abc")查询某个子串在s中最后一次出现的下标；如果不存在，则返回-1。
当不知道读入的具体行数时，可以采用如下方法一次性读取所有行：
from sys import stdin

for line in stdin.readlines():
    print(line.strip())  # strip()是为了去掉行末的回车

'''