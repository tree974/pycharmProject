# ---- 数据类型 ----
# 基本数据类型: 都是不可变
# (可变对象:创建后,内存里本身的数据可以直接修改,对象地址不变;不可变对象:创建后,内存里原始数据不能改动,如果要改只能新建对象)
# 数值型：整数int、浮点数float、复数complex、布尔bool

# 容器数据类型：
# 字符串str(不可变)、列表list、元组tuple(不可变)、集合set、字典dist

# 特殊数据类型：
# None：表示空值或者缺失值，常用于函数没有返回值时，或者变量没有赋值时

# --- int型 ---
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

# --- float型 ---
num1 = 0.1
num2 = 0.2
print(num1 + num2) # 0.30000000000000004

from decimal import Decimal # 引入函数
num3 = Decimal('1.0')
num4 = Decimal('0.9')
print(num3 - num4)

# --- bool型 ---
# python3中,bool是int的子类,True=1,False=0
bool1 = True
bool2 = False
print(bool1, bool2)
print(bool1 + 1) # 2
print(True == 1) # True


# --- str型 ---
# 1.反斜杠表示转义
str1 = 'hello\n'
str2 = "\thello\""
print(str1, str2)
# 2.3个引号表示多行字符串
str3 = """ 
abc
"""
print(str3)
# 3.intern机制,相同字符串,共享内存,只保留一份
str4 = 'a'
str5 = 'a'
print(str4 is str5) # True; is运算符,用于比较两个对象是否为同一个对象,是否在内存中占据相同的位置

# --- 数据类型转换 ---
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


# --- 字符的编码和解码 ---
str1 = '你好'
byte1 = str1.encode("utf8")
print(byte1)       # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(byte1)) # <class 'bytes'>
str2 = byte1.decode("utf8") # 使用什么编码集,就要使用它解码
print(str2)        # 你好
print(type(str2))  # <class 'str'>

# --- 输入和输出 ---
input_str = input('请输入: ') # 输入的类型,都会转为字符串变量
print('input_str数据类型为: ', type(input_str), end='123\n') # print输出,end=表示用什么结尾
# 格式化输出
int1 = 10
float1 = 3.14
str1 = "int1 = %d, float1 = %f" % (int1, float1) # 中间的%格式化操作符,是把右边括号里的数据,依次填入左边模板中对应的%占位符
print(str1)
str2 = "int1 = {}, float1 = {}".format(int1, float1)
print(str2)
# 设置指定位置,按照位置填写
str3 = "int1 = {1}, float1 = {0}".format(float1, int1) #int1 = 10, float1 = 3.14
print(str3)
# 数字格式化
str4 = "{:*^20,.2f}".format(float1)
print(str4) # ********3.14********
# 使用大括号{}来转义大括号
print("{0}对应的位置是{0}".format("hello")) # hello对应的位置是hello,字符串中的数字是占位符
print("{}对应的位置是{{0}}".format("hello")) # hello对应的位置是{0},不带数字自动按顺序占位
# f-字符串,字符串前加一个f,字符串中的{}内写变量名
str5 = f"int1 = {int1}, float1 = {float1}"
print(str5) # int1 = 10, float1 = 3.14
# {}内变量后可以加上=,打印时会在变量值前加上 变量名=
str6 = f"{int1 = }, {float1 =}"
print(str6) # int1 = 10, float1 =3.14
# {}外再套一层{},即{{}}会转义
str7 = f"{{int1 = }}, {{float1 = }}"
print(str7) #{int1 = }, {float1 = }
str8 = f"{{888}}"
print(str8)



# --- 运算符 ---
# 成员运算符
num6 = 1
num7 = 2
test_list = [1,3,5]
print(num6 in test_list)
print(num7 not in test_list)



# ---- 容器 ----
# 序列: 有序存储和操作数据,可以包含不同类型的元素,支持通过索引访问和修改元素
# --- list ---
list1 = [1,2,3,4,5] # 最后一个坐标是-1
print(list1)
# 通过索引取数据
print(list1[0])
print(list1[-2]) # 4
print(list1[-4]) # 2
# 列表切片
print(list1[:])    # 复制整个列表
print(list1[2:4])  # 取索引从2开始到4的元素(不包含4)
print(list1[2:])   # 取索引从2开始到末尾的元素
print(list1[:2])   # 取索引从0开始到2(不包含2)的元素
print(list1[2:-1]) # 取索引从2开始到-1(不包含)的元素
print(list1[::-1]) # 倒叙取元素
# 向列表中添加元素
list1.append(6)
list1.insert(0, 7) # 指定位置前添加元素
print(list1)
# 列表相加
list2 = ['a', 'b', 'c']
print(list1 + list2)
# 列表乘法,不是每个元素乘法,而是整个列表复制一份
print(list1 * 2)
# 修改列表中元素
list2[0] = 'aa'    # 通过坐标修改
print(list2)
list2[0:2] = ["aaa",'bbb'] # 通过切片修改
print(list2)
# 检查成员是否为列表中元素
print('aaa' in list2)
# 获取列表长度
print(len(list2))
# 求列表中元素的最大值、最小值、和
print(max(list1))
print(min(list1))
print(sum(list1))
# 遍历列表
for i in list1:
    print(f"列表中的元素, {i}")
for i in range(len(list1)):
    print(i, list1[i]) # 通过下标遍历
for i, val in enumerate(list1):
    print(i, val)      # 通过enumerate同时获取列表下表和元素
# 删除列表指定位置元素或者切片
del list1[0]
print(list1)
# 嵌套列表,列表元素也可以为列表
list3 = [[1,2],[3,4],[5,6]]
print(list3)
# 列表推导式: 创建列表的方式2
squares = [x**2 for x in range(5)]               # 基础的列表推导式,**2表示平方
print(squares)  # 0,1,2,3,4 -> 0,1,4,9,16
squares = [x**2 for x in range(5) if x % 2 == 0] # 带条件的列表推导式
print(squares)
squares = [x**2 for x in list1]                  # 使用现有列表的列表推导式
print(squares)
tuple_list = [(i, j) for i in list1 for j in list2]
print(list1)
print(list2)
print(tuple_list)
list4 = [1,2]
tuple_list = [(i**2, j**2) for i in list1 for j in list4] # 也可以直接i的平方
print(tuple_list)
# zip函数: 将多个list对应元素打包为一个个元组; 注意: 元素不会笛卡尔积,只有相同位置的元素才会打包成一个元组
zipped = zip(list1,list4)
print(list(zipped)) # [(1, 1), (2, 2)]. zip函数返回的是一个迭代器对象,如果直接打印zipped,只会输出内存地址,通过list(zipped)相当于一次性遍历迭代器,收集起来变成列表
print(list(zipped)) # []. 注意: 迭代器只能遍历一次,下次后再打印就是空的

# --- 字符串:不可变的,有序的,字符串中元素不能修改 ---
str8 = 'abcd'
print(str8[:])  # abcd
print(str8[0])  # a
print(str8[0:2])# ab
print(str8[2:]) # cd
print(str8[:2]) # ab
print("ab" in str8) # 检查成员是否在字符串中
print("hello\nworld")  #转义字符串
print(r"hello\nworld") #原始字符串,加r不转义


# ---- 元组:不可变,有序的元素集合,不能对元组内的元素进行修改,元素可以是不同类型 ----
print(type((10)))    # int
print(type((10,)))   # tuple,如果元组中只有1个元素,需要加逗号

tuple_generator = (x for x in range(10))
print(tuple_generator)
tuple1 = tuple(tuple_generator) # list是[]，元组是()
print(tuple1)

tuple1 = (1,2,3)
print(id(tuple1), tuple1)
tuple1 = tuple1 + (4,5)
print(id(tuple1), tuple1) # id变了,说明元组中的不可变:所指向的内存中的内容不可变,但可以重新赋值

tuple1 = (100, 200, 300, [1, 2, 3]) # 如果元组中的元素是可变数据类型,其嵌套项(比如list)可以改变
print(id(tuple1))
tuple1[3].append(4)
print(tuple1) # (100, 200, 300, [1, 2, 3, 4])
print(id(tuple1)) # id没有变(因为list的地址没变,只是改了它的值,所以元组地址没变)



# ----set集合:无序,{}定义----
set1 = {1,2,3}
set2 = set([1,2,3])
set3 = set()
print(set1)
print(set2)
print(set3)
set1 = {x for x in range(10) if x % 2 == 0}


# ---- 字典dictionary:无序键值对集合,{}定义,每个键值对之间用逗号分隔 ----
dict1 = {}
dict2 = dict()
dict3 = {"name":"zs", "age":18}
dict4 = dict(name="zs", age=18)
dict5 = dict([("name","zs"),("age",18)])
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
squares = {x: x**2 for x in range(4)}
print(squares)

dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print(dict1["name"])
print(dict1.get("name","a"))
dict1["address"] = "earth" # 添加元素
del dict1["address"]
del dict1
dict1.clear()


# 区别
"""
数据结构    是否可变    是否重复    是否有序(有下标,多次遍历顺序一致)    如何定义
列表         是         是          是        []
元组         否         是          是        ()
字典         是        key不允许     否        {}
集合         是         否          否        {}        
"""
# 可变:指的是对象中的元素可变,元素变后,该对象的地址不会变;比如list=[1,2],list[0]=3,id(list)不会变
# 不可变:对象中的元素不可变,变了后,直接就是新对象(tuple新增/删除元素都是另一个tuple,除非修改的是元组中的可变元素(list))
# 可变与不可变侧重点是值是否可变,只要对象重新赋值,id(对象)都会变

























