# __all__只有2个元素
from PackageOp import *  # 局部导入from import
print(add(1, 2))
print(num)
# print(num1) # NameError: name 'num1' is not defined. Did you mean: 'num'?




import PackageOp # 全局导入模块,可使用所有元素,不受__all__影响
print(PackageOp.add(1, 2))
print(PackageOp.num)
print(PackageOp.num1)


# dir():主要列出对象的属性和方法,或者列出当前作用域下定义的名称
# 模块作为参数,会返回该模块中定义的名称列表(函数、类、变量等)
print(dir(PackageOp)) # ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_str1', 'add', 'num', 'num1']


class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2
    def method1(self):
        pass
obj = MyClass()
print(dir(obj)) # 如果是一个对象作为dir()的参数,它会返回该对象的属性和方法列表

# 不传递任何参数,会返回当前作用域中定义的名称(变量、函数、类等)
print(dir())


