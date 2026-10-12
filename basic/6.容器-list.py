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
print(3 in listx) # 判断元素是否在list