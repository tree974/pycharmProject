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

def decorator1(func):
    def inner(x):
        x = abs(x) # 在不修改原函数的前提下,给原函数增加绝对值功能
        return func(x)
    return inner

@decorator1    # 等价于func = decorator1(func),注意: 这个@decorator1,必须要定义了这个方法后才能使用
def func(x):
    return sqrt(x)
# func = decorator(func) # 这里的func==inner,这里的func就相当于给老函数的func增加了功能
print(func(-4)) # func(-4)->inner(-4)->abs(-4)->func(4)



print("----多层装饰器----")
# ----多层装饰器:离函数最近的装饰器先装饰,然后外面的装饰器再进行装饰----
# 将参数转为整型
def get_integer(fun1):
    print(f"进入get_integer函数")
    def inner1(x):
        print(f"进入inner1函数")
        x = int(x)
        return fun1(x)
    return inner1

# 将参数转为非负数
def get_absolute(fun1):
    print(f"进入get_absolute函数")
    def inner2(x):
        print(f"进入inner2函数")
        x = abs(x)
        return fun1(x)
    return inner2

# 包装顺序: 从下往上,越靠近func1的装饰器,最先包装.先转为绝对值,然后转为int型
@get_integer
@get_absolute # 位置近的先执行,如果交换位置就会报错
def fun1(x):
    return sqrt(x)

print(fun1("-9"))

"""
执行流程:
1.先定义原始函数def func1(x);
注意: 
    ①包装过程: 装饰器函数,只负责接收函数,生成inner,不是处理参数x的逻辑
    ②执行过程: 是调用func1()的时候
    ③注意,每个装饰器实际传入的参数,比如get_integer实际传入的是inner2
2.先执行靠下面的@get_absolute装饰器: func1 = get_absolute(func1) = inner2
3.再执行上面的@get_integer装饰器: fun1 = get_integer(inner2)此时fun1变成了inner2 = inner1, 此时其实func1 = inner1
4.调用: func1("-9") -> inner1("-9") -> 转成整数 -> 此时的fun1是inner2(-9) -> 取绝对值-> func1(9) -> 3

原始fun1（sqrt）
    ↓ 被 get_absolute 包一层 → inner2
        ↓ 被 get_integer 再包一层 → inner1
fun1 变量现在 = inner1
"""
