# ----动态添加属性与方法----
import types


class Person:
    # __slots__限制实例属性与方法
    # 如果有属性放在了__slots__中,那么就不要手动再给类上赋值同名的类属性
    __slots__ = ("name", "age", "eat", "eat1") # 此时属性和方法名只能是这个列表中的,在这之外的不能添加
    def __init__(self,name):
        self.name = name

# 动态给类增加 类属性
Person.age1 = 10
print(Person.age1) #10

# 动态给对象增加 属性
p = Person("zs")
p.age = 20
print(p.age) #20

# 动态给类增加方法
# 1.增加类方法
@classmethod
def come_from(cls):
    print(f"给类增加类方法,age={cls.age}")
Person.come_from = come_from
Person.come_from() # 给类增加类方法,age=10
# 2.增加静态方法
@staticmethod
def static_method():
    print("static function")
Person.static_method = static_method
Person.static_method() # static function

# 动态给对象增加方法
# 1.增加普通方法
def eat():  # 注意给对象添加没有self,只有类空间下的方法才有self
    print("给对象添加普通方法")
p.eat = eat
p.eat() # 给对象添加普通方法
# 2.增加实例方法,只绑定在当前对象,对其他对象不生效
def eat1(self):
    print(f"给对象添加实例方法,name={self.name}正在吃饭")
p.eat1 = types.MethodType(eat1, p)
p.eat1() # 给对象添加实例方法,name=zs正在吃饭
# 动态删除属性与方法,删除后再调用就会报错
del p.eat1
# delattr(p, eat1)
# p.eat1()


# 测试__slots__限制实例属性和方法
def eat2():
    print("eat2方法在__slots__之外")
p.eat2 = eat2 # 由于eat2是在__slots__之外的,所以不能添加成功
p.eat2()