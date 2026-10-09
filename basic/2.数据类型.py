# ---- 数据类型 ----
# 基本数据类型: 都是不可变
# (可变对象:创建后,内存里本身的数据可以直接修改,对象地址不变;不可变对象:创建后,内存里原始数据不能改动,如果要改只能新建对象)
# 数值型：整数int、浮点数float、复数complex、布尔bool

# 容器数据类型：
# 字符串str(不可变)、列表list、元组tuple(不可变)、集合set、字典dist

# 特殊数据类型：
# None：表示空值或者缺失值，常用于函数没有返回值时，或者变量没有赋值时


# ------- int型 -------
# 1.整数分隔符_
num1 = 1_000_000_000_000_000 # 书写很大的数,可以使用_分隔符
print(num1) # 1000000000000000

# 2.type和isinstance类型判断
"""
type: 查看变量类型,且不会认为子类是父类
isinstance: 判断变量类型,且会认为子类是父类
"""
num1 = True
num2 = 10
print(type(num1)) # <class 'bool'>
print(type(num2)) # <class 'int'>
print(type(num1) == type(num2))  # False
print(isinstance(num1, bool)) # True
print(isinstance(num1, int))  # True,python3中,bool是int的子类
print(isinstance(num2, int))  # True
# 3.小整数池、大整数池
smallInt1 = 260
smallInt2 = 260
print("小整数池[-5,256]里创建的所有变量都是指向同一个对象,但范围之外的不一定就是不同对象: ", smallInt1 is smallInt2)


# -------- float型 --------
num1 = 0.1
num2 = 0.2
print(num1 + num2) # 0.30000000000000004

from decimal import Decimal # 引入函数
num3 = Decimal('1.0')
num4 = Decimal('0.9')
print(num3 - num4) # 0.1


# -------- 复数类型 --------
"""
# 复数类型,一般用作科学计算、信号处理领域,后端一般用不到
z = 0 + 0j
c = -0.7 + 0.27j
for _ in range(10):
    z = z**2 +c
print(z)
"""


# -------- bool型 --------
# python3中,bool是int的子类,True=1,False=0
bool1 = True
bool2 = False
print(bool1, bool2)
print(bool1 + 1) # 2
print(True == 1) # True


# -------- str型 --------
# 1.反斜杠表示转义
str1 = 'hello\n'
str2 = "\thello\""
print(str1, str2)
# 2.3个引号表示多行字符串,所见即所得
str3 = """ 
abc
"""
print(str3)
# 3.intern机制,相同字符串,共享内存,只保留一份
str4 = 'a'
str5 = 'a'
print("intern机制: ", str4 is str5) # True; is运算符,用于比较两个对象是否为同一个对象,是否在内存中占据相同的位置


# -------- 数据类型转换 --------
# 自动类型转换(隐式转换): 两种不同类型数据运算,较小数据类型会转成较大数据类型计算
num1 = 2            # int
num2 = 3.0          # float
print(num1 - num2)  # -1.0 float
num3 = 1
print(num1 / num3)  # 2.0; 特别的,两个整数进行除法,结果也是float
# 强制类型转换: 通过函数对数据类型进行转换
x = "111"
print(type(x))      #<class 'str'>
print(type(int(x))) # <class 'int'>
print(isinstance(int(x), int)) # True


# -------- 字符的编码和解码 --------
str1 = '你好'
byte1 = str1.encode("utf8")
print(byte1)       # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(byte1)) # <class 'bytes'>
str2 = byte1.decode("utf8") # 使用什么编码集,就要使用它解码
print(str2)        # 你好
print(type(str2))  # <class 'str'>
















