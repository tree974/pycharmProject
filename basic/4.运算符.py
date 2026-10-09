# -------- 运算符 --------
# 成员运算符
num6 = 1
num7 = 2
test_list = [1,3,5]
print(num6 in test_list)
print(num7 not in test_list)

# 身份运算符
m = 20
n = 20
print(id(m))
print(id(n))
print(id(m) == id(n)) #True

# is和==的区别
a = [1,2,3]
b = a
print(b is a) # True,is比较的是地址
print(b == a) # True,==比较的是值
b = a[:] # [1, 2, 3]
print(b)
print(b is a) # False
print(b == a) # True

# 海象运算符: 在表达式内部完成赋值,同时返回赋值后的值
from random import randint
print("此人的年龄为", age := randint(0,100))
# 等价于下面的语法：
age = randint(0, 100)
print("此人年龄为", age)
