# python高级语法：浅拷贝和深拷贝
"""
直接赋值：对象的引用(别名), 不产生拷贝
浅拷贝：拷贝父对象,不会拷贝对象的内部的子对象。拷贝后只有第一层是独立的
    1. 切片操作,如[:]
    2. 使用工厂函数,如list(), set()
    3. 使用copy模块的copy()函数
深拷贝：完全拷贝了父对象及其子对象。拷贝后所有层都是独立的。注意: 拷贝后的新对象只有可变类型地址才会发生新变化

不管是浅拷贝还是深拷贝,子对象如果是可变类型,对可变类型进行值的改变,都不会使地址发生变化.
只有深拷贝后的新对象中的可变类型地址,拷贝完后会发生变化
"""


# ----浅拷贝: list1本身是父对象,而里面的所有元素是子对象,里面的子对象共用一个----
import copy
list1 = [1,2,3,[4,5,6]]
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3]))

list2 = copy.copy(list1)
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3]))
# list2中的所有子元素地址都没有变化,但list2本身地址变化了

# 1.修改list1中的元素
list1[0] = 100
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3])) # list1[0]为不可变元素,所以值变后,指向了一个新的对象,地址就变了
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3])) # 由于list2是copy后的新对象,里面的list2[0]并没有变,所以地址没变

# 2.修改list1[3]可变元素中的元素
list1[3].append(7)
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3])) # list1[3]是可变元素,里面元素发生变化,并不会导致地址变化
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3])) # list2[3]指向的也是list1[3],地址也没变
# print(list2[3])



# ---- 深拷贝 ----
print("-----深拷贝-----")
import copy
list1 = [1,2,3,[4,5,6]]
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3]))

list2 = copy.deepcopy(list1)
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3]))
# list2本身、可变子对象list的地址发生了变化(list1[3]和list2[3]不一样了),其他不可变类型对象地址没有变化


# 1.修改list1中的元素
list1[0] = 100
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3])) # list1[0]为不可变元素,所以值变后,指向了一个新的对象,地址就变了
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3])) # 由于list2是copy后的新对象,里面的list2[0]并没有变,所以地址没变

# 2.修改list1[3]可变元素中的元素
list1[3].append(7)
print(id(list1), id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3])) # list1[3]是可变元素,里面元素发生变化,并不会导致地址变化
print(id(list2), id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3])) # list2[3]指向的本来就不是list1[3],所以值不会变
print(list2[3]) # 打印的不是list1[3]的值了: [4, 5, 6]


# ----拷贝的特殊情况----
print("拷贝的特殊情况...")
# 非容器类型,无法拷贝.地址都不会发生变化
var1 = 1
print(id(var1), var1) # 140706434216744 1
var2 = copy.copy(var1)
print(id(var2), var2) # 140706434216744 1
var3 = copy.deepcopy(var1)
print(id(var3), var3) # 140706434216744 1

# 元组变量如果只包含原子类型对象,则不能对其深拷贝
tuple1 = (1,2,3) # 元组只包含原子类型对象
print(id(tuple1), tuple1) # 1497062403968 (1, 2, 3)
tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2) # 1497062403968 (1, 2, 3)

tuple1 = (1,2,3,[]) # 元组不只包含原子类型对象,深拷贝后地址会发生变化
print(id(tuple1), tuple1) # 2337065491712
tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2) # 2337068356832 地址发生变化

