# 面向对象: 首先定义每个对象,然后将所有对象的属性和行为封装打包到一起，封装成类
# 3大特征: 封装、继承、多态
class Person:
    """人的类"""
    home = "earth" # 类属性最好和实例属性不要同名
    def __init__(self, name, age): # 构造方法,self相当于创建对象的实例,比如 x = Person("zs",10),那self=x
                                   # 自动将p这个新建对象传给init的第一个参数self
                                   # 构造方法只能返回None
        self.name = name
        self.age = age

    def eat(self): # 实例方法(非静态方法)第一个形参是该对象,必须要加上,调用的时候可以不传入
        print("eating...")

    def drink(self):
        print("drinking...")
    @classmethod # 类方法,cls是类本身,可以通过cls去创建对象
    def get_home(cls):
        c = cls("cls创建的对象", 10) # 通过类创建一个对象
        print(f"通过cls创建一个对象,调用属性: {c.name}")
        return cls.home

    @staticmethod
    def static_method(): # 无法访问类或实例的信息,更像是一个工具类,为了方便组织代码,把它放在了类里面
        print(f"这是静态方法,类属性为: {home1}") # 注意: 这个home1是下面定义的全局变量,这里只是定义,只有当真正调用这个方法时,才会去寻找这个变量(延迟寻找)
        # print(f"这是静态方法,类属性为: {home}") # 注意: 静态方法是不能直接访问类属性和实例信息的
        print("这是静态方法")

# 类直接调用
home1 = Person.home # 获取一个字符串
print(home1) #  earth
eat_func = Person.eat # 没有调用,所以打印的是地址
print(eat_func) # <function Person.eat at 0x0000018BA0457380>
doc = Person.__doc__ # 类的注释
print(doc) # 人的类
Person.static_method() # 只有在调用这个静态方法时,才会去寻找这个变量,如果找不到就会报错

# 对象调用
p = Person("zs", 18)
print(p)
print(p.name)
print(p.age)
p.eat() # 相当于调用了Person.eat(p) # eating...
print("调用类方法:"+Person.get_home())  # earth
print("调用类方法:",Person.get_home())  #  earth,如果双引号后跟的逗号,那么输出时逗号位置就是空格
Person.static_method()
p.static_method()
"""
实例方法: 只能实例调用,如果是类直接调用(Person.eat(p对象))
类方法: 类/实例都可以调用,自动传cls
静态方法: 类/实例都可以调用,什么都不传,但静态方法不能访问类和对象信息
"""


# 类外定义方法
# 也可以在类外定义方法,将一个函数对象赋值给类变量
# 只有挂在类空间的方法,调用时才会自动传入self.如果直接挂在实例上,就是普通方法,不会自动传self
def f1(self, x, y):
    print(f"类外定义方法,传递给类变量: {x * y}")
class C:
    f = f1 # 把类外方法传递给类变量

    def f2(self):
        return self

C().f(6,1) # 创建一个实例,由于f1传给了类变量f,那么f就是类方法了,直接调用即可
C().f2().f(6,1) # f2 return的是C()这个实例,所以相当于是实例.类方法

