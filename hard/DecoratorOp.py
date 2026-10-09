# 装饰器: 允许在不修改原有函数代码的基础上,动态增加或修改函数的功能
# 本质是一个接收函数作为输入,并返回一个新的包装过后的函数的对象

"""
相当于就是给函数外面包了一层,返回一个新的函数(内层函数)
def decorator(func): # 接收函数func作为参数
    def inner(参数):  # 内部函数,可以执行一些额外操作,然后调用原始函数func
        # 添加功能
        func(参数)
        # 添加功能
    return inner     # 返回一个内部函数inner
"""

# 闭包实现装饰器
from math import sqrt

def decorator(func):
    def inner(x):
        x = abs(x) # 在不修改原函数的前提下,给原函数增加绝对值功能
        return func(x)
    return inner

@decorator    # 等价于func = decorator(func),注意: 这个@decorator,必须要定义了这个方法后才能使用
def func(x):
    return sqrt(x)

"""
语法: 
@xxx # 这里的xxx就是之前定义好的装饰器函数名,等价于test = xxx(test)
def test():
    pass
"""

# func = decorator(func) # 这里的func==inner,这里的func就相当于老函数的func增加了功能
print(func(-4)) # func(-4)->inner(-4)->func(4)




# ----多层装饰器:离函数最近的装饰器先装饰,然后外面的装饰器再进行装饰----
# 将参数转为整型
def get_integer(fun1):
    def inner(x):
        x = int(x)
        return fun1(x)
    return inner

# 将参数转为非负数
def get_absolute(fun1):
    def inner(x):
        x = abs(x)
        return fun1(x)
    return inner

# 包装顺序: 从下往上,越靠近func1的装饰器,最先包装
@get_integer
@get_absolute # 位置近的先执行,如果交换位置就会报错
def fun1(x):
    return sqrt(x)

print(fun1("-9"))

