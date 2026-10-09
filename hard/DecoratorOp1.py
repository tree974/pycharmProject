# ----带参数的装饰器----
from math import sqrt
# 求根号n次
def times(n):
    # 将参数转为非负数
    def get_absolute1(f):
        def inner1(x):
            x = abs(x)
            for i in range(n): # 执行2次,第一次4 = f(16),第二次2 = f(4)
                x = f(x)
            return x
        return inner1
    return get_absolute1

@times(2)
def func2(x):
    return sqrt(x)

print(func2(-16))


# ----类装饰器:包含__call__()方法的类,接收函数作为参数,并返回新的函数----
class DecoratorClass:
    def __init__(self, func):
        self.func = func
    def __call__(self, x):
        print("触发__call__方法")
        x = abs(x)
        return self.func(x)

# @DecoratorClass
def func(x):
    return sqrt(x)

func = DecoratorClass(func) # 这里返回的是装饰类的改造后的方法,将func传入
print(func(-16)) # func()调用的时候自动会触发__call__方法,此时传入的x=-16,取绝对值后,再调用原本的func