# ---- 元组 ----
"""
不可变,有序的元素集合;
不能对元组内的元素进行修改;
使用()定义,数据之间使用,分隔
元组也有下标
可以是不同类型
"""
print(type((10)))    # int
print(type((10,)))   # tuple,如果元组中只有1个元素,需要加逗号

tuple_generator = (x for x in range(10)) # 注意,这里不是列表推导式,是生成器表达式
print(tuple_generator) # <generator object <genexpr> at 0x000001D2243D5A80>
tuple1 = tuple(tuple_generator) # 转换为元组,list是[]，元组是()
print(tuple1) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

tuple1 = (1,2,3)
print(id(tuple1), tuple1) # 2959790466816 (1, 2, 3)
tuple1 = tuple1 + (4,5)   # 2959790600448 (1, 2, 3, 4, 5)
print(id(tuple1), tuple1) # id变了,说明元组是不可变

tuple1 = (100, 200, 300, [1, 2, 3]) # 如果元组中的元素是可变数据类型,其嵌套项(比如list)可以改变
print(id(tuple1))
tuple1[3].append(4)
print(tuple1) # (100, 200, 300, [1, 2, 3, 4])
print(id(tuple1)) # id没有变(因为list的地址没变,只是改了它的值,所以元组地址没变)
