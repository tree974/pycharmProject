# ---- 容器 ----

"""
序列: list、tuple、字符串
有序存储和操作数据(索引、切片、相加、乘法、检查成员、计算长度、计算最大值最小值)
可以包含不同类型的元素
支持通过索引访问和修改元素
"""

# -------- list --------
list1 = [1,2,3,4,5] # 最后一个坐标是-1
print(list1)
# 通过索引取数据
print(list1[0])  # 2
print(list1[-2]) # 4
print(list1[-4]) # 2
# 列表切片
print(list1[:])    # 复制整个列表 [1, 2, 3, 4, 5]
print(list1[2:4])  # 取索引从2开始到4的元素(不包含4) [3, 4]
print(list1[2:])   # 取索引从2开始到末尾的元素 [3, 4, 5]
print(list1[:2])   # 取索引从0开始到2(不包含2)的元素 [1, 2]
print(list1[2:-1]) # 取索引从2开始到-1(不包含)的元素 [3, 4]
print(list1[::-1]) # 倒叙取元素  [5, 4, 3, 2, 1]
# 向列表中添加元素
list1.append(6)
list1.insert(0, 7) # 指定位置前添加元素
print(list1) # [7, 1, 2, 3, 4, 5, 6]
# 列表相加
list2 = ['a', 'b', 'c']
print(list1 + list2) # [7, 1, 2, 3, 4, 5, 6, 'a', 'b', 'c']
# 列表乘法,不是每个元素乘法,而是整个列表复制一份
print(list1 * 2) # [7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6]
# 修改列表中元素
list2[0] = 'aa'    # 通过坐标修改 ['aa', 'b', 'c']
print(list2)
list2[0:2] = ["aaa",'bbb'] # 通过切片修改 ['aaa', 'bbb', 'c']
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
    if (i == len(list1)-1):
        print(i, list1[i])
    else:
        print(i, list1[i], end = ",") # 通过下标遍历

for i, val in enumerate(list1):
    print(i, val, end = ",")      # 通过enumerate同时获取列表下表和元素
print()

# 删除列表指定位置元素或者切片
del list1[0]
print(list1) # [1, 2, 3, 4, 5, 6]

# 嵌套列表,列表元素也可以为列表
list3 = [[1,2],[3,4],[5,6]]
print(list3)

# 列表推导式: 创建列表的方式2
squares = [x**2 for x in range(5)]               # 基础的列表推导式,**2表示平方
print(squares)  # 0,1,2,3,4 -> 0,1,4,9,16
squares = [x**2 for x in range(5) if x % 2 == 0] # 带条件的列表推导式
print(squares) # [0, 4, 16]
squares = [x**2 for x in list1]                  # 使用现有列表的列表推导式
print(squares) # [1, 4, 9, 16, 25, 36]

tuple_list = [(i, j) for i in list1 for j in list2]
print(list1)  # [1, 2, 3, 4, 5, 6]
print(list2)  # ['aaa', 'bbb', 'c']
print(tuple_list) # [(1, 'aaa'), (1, 'bbb'), (1, 'c'), (2, 'aaa'), (2, 'bbb'), (2, 'c'), (3, 'aaa'), (3, 'bbb'), (3, 'c'), (4, 'aaa'), (4, 'bbb'), (4, 'c'), (5, 'aaa'), (5, 'bbb'), (5, 'c'), (6, 'aaa'), (6, 'bbb'), (6, 'c')]
list4 = [1,2]
tuple_list = [(i**2, j**2) for i in list1 for j in list4] # 也可以直接i的平方
print(tuple_list) # [(1, 1), (1, 4), (4, 1), (4, 4), (9, 1), (9, 4), (16, 1), (16, 4), (25, 1), (25, 4), (36, 1), (36, 4)]

# zip函数: 将多个list对应元素打包为一个个元组; 注意: 元素不会笛卡尔积,只有相同位置的元素才会打包成一个元组
zipped = zip(list1,list4) # [(1, 1), (2, 2)]
print(list(zipped)) # [(1, 1), (2, 2)]. zip函数返回的是一个迭代器对象,如果直接打印zipped,只会输出内存地址,通过list(zipped)相当于一次性遍历迭代器,收集起来变成列表
print(list(zipped)) # []. 注意: 迭代器只能遍历一次,下次后再打印就是空的

# list相关的方法
listx = [1,2,3,4]
listx1 = [6]
listx.insert(0,0)
listx.append(5)
listx.extend(listx1) # 列表1的基础上追加列表2
print(listx) # [0, 1, 2, 3, 4, 5, 6]
del listx[0] # 删除指定下标的元素
listx.remove(2) # 删除第一次出现的x
print(listx) # [1, 3, 4, 5, 6]

listx.pop() # 默认删除最后一个元素
listx.pop(1) # 删除下标为1的元素
print(listx) # [1, 4, 5]
listx2 = [3]
listx[0:1] = listx2 # 切片方式赋值
print(listx)

# 列表反转的几种方式
listx3 = sorted(listx, reverse=True)
print(listx3) # [5, 4, 3]
listx.sort(reverse=True)
print(listx)  # [5, 4, 3]
listx.reverse()
print(listx) # [3, 4, 5]

print(listx.index(5)) # 返回x在列表中第一次出现的位置
print(listx.count(3)) # 返回列表的个数
print(len(listx))

print(max(listx))
print(min(listx))
print(sum(listx))
print(listx.copy())    # [3, 4, 5]
print(list(listx)) # 将序列转为列表 [3, 4, 5]
print(3 in listx) # 判断元素是否在list中





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




