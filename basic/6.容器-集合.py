# ----set集合:无序,{}定义----
setx = {} # 空集合不能使用{},这样创建的是空字典,要使用set()
print(type(setx)) # <class 'dict'>
setx = set()
print(type(setx)) # <class 'set'>

# 创建set方式:
set1 = {1,2,3}
set2 = set([1,2,3])
set3 = set()
print(set1)
print(set2)
print(set3)
set1 = {x for x in range(10) if x % 2 == 0}


# set的其他方法
# 合并
set4 = {1,2,3,4,5}
set4.update([4,5,6]) # 将其他类型的数据合并到集合中,自动去重,修改原集合
print(set4) # {1, 2, 3, 4, 5, 6}
set5 = {1,2,3,4,5}
print(set5.union([4,5,6]))  # 将其他类型的数据合并到集合中,自动去重,但返回一个新的集合 {1, 2, 3, 4, 5, 6}
print(set5) # {1, 2, 3, 4, 5} # 原集合没变

set6 = {1,2,3,4,5,6}
set6.remove(1) # {2, 3, 4, 5, 6}, 移除元素,不存在则报错
set6.discard(2) # {3, 4, 5, 6}, 移除元素,不存在不报错

set7 = {"a", "b", "c"}
set7.pop() # {'a', 'b'}, 随机弹出一个元素,不能保证每次弹出都是同一个元素

# 判断逻辑
set8 = {4,5}
set9 = {5,6}
print(set8.isdisjoint(set9)) # False,判断两集合是否没有交集,没有交集为true,有交集为false
print(set8.symmetric_difference(set9)) # {4, 6},求两集合中不重复的元素,返回一个新的集合
set8.symmetric_difference_update(set9) # 求两集合中不重复的元素,直接返回给原集合
print(set8) # {4, 6}
print(set9) # {5, 6}

set8 = {4,5}
set9 = {4,5,6}
print(set8.issubset(set9)) # True,判断set1是否为set2的子集
print(set8.issuperset(set9)) # False,判断set2是否为set1的子集

print(sum(set8)) #9

set9 = set8.copy()
print(f"set8拷贝后的集合: {set9}") # {4, 5}

# 数学运算: 差集、交集
# 差集
set8 = {4,5}
set9 = {5,6}
print(set8.difference(set9)) # {4},求差集,返回一个新的集合
print(set8.difference_update(set9)) # None,求差集,直接返回给原集合,即set8
print(set8) # {4}
print(set9) # {5, 6}
print(set8 - set9) # {4}
# 交集
set8 = {4,5}
print(set8.intersection(set9)) # {5},求交集,返回一个新的集合
set8.intersection_update(set9) # 求交集,直接返回给原集合,即set8
print(set8) # {5}
print(set9) # {5, 6}
set8 = {4,5}
print(set8 & set9) # {5}
print(set8) # {4, 5}
print(set9) # {5, 6}















