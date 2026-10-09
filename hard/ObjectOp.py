# 面向对象: 首先定义每个对象,然后将所有对象的属性和行为封装打包到一起，封装成类
# 3大特征: 封装、继承、多态
class Person:
    """人的类"""
    home = "earth"
    def __init__(self, name, age): # 构造方法,self相当于创建对象的实例,比如 x = Person("zs",10),那self=x
                                   # 自动将p这个新建对象传给init的第一个参数self
        self.name = name
        self.age = age

    def eat(self):
        print("eating...")

    def drink(self):
        print("drinking...")

home = Person.home # 获取一个字符串
eat_func = Person.eat
doc = Person.__doc__

print(home)
print(eat_func)
print(doc)


p = Person("zs", 18)
print(p)
print(p.name)
print(p.age)
p.eat() # 相当于调用了Person.eat(p)




# ---- 封装 ----
# 私有化:为了限制属性和方法只能在类内访问,外部无法访问; 或父类中某些属性和方法不希望被子类继承
# 单下划线: 非公开API,_var1
# 双下划线: 有2个前缀下划线,并至多一个后缀下划线,如__x,会被改写为_类名_x。①类内可以通过__x访问;②其他地方只能通过_类名__x访问
# @property:
#   ①用在普通方法上,即可将方法转为属性,直接对象.方法名调用,不用加();
#   ②如果是私有属性__name,用在属性名方法上(不加__),此时私有属性变成了只读属性
#   ③用property修饰的方法,不要和类变量重名,否则会无限循环
class Person:
    def __init__(self, name):
        self.__name = name   # name是私有属性
    def get_name(self):
        return self.__name  # 私有属性可通过类内 __name访问
    def __private_method(self): # 私有方法
        print("这是一个私有方法")

    @property   # 可将方法转为属性
    def eat(self):
        print(f"{self.__name} is eating...")
    @property
    def name(self):
        return self.__name # 变成了只读属性,p.name = '李四'报错
    @name.setter
    def name(self, new_name):
        self.__name = new_name # 变成了读写属性,可通过p.name = '李四'

p = Person("张三")
print(p.get_name())
print(p._Person__name)     # 私有属性可通过类外 _类__name访问
# print(p.__name) # 报错
# print(p.__private_method())# 报错
p._Person__private_method()# 私有方法可通过类外 _类__方法名访问

p.eat    # 直接调用属性即可
print(p.name)



# ----继承----
class Person:
    home = "earth"
    def __init__(self, name):
        self.__name = name
    def eat(self):
        print(f"{self.__name} is eating...")

class YellowRace(Person): # 继承Person
    color = "yellow"

y = YellowRace("zz")
print(y.color)
y.eat()

# 多继承:java只能接口多实现,类不能多继承
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name) # 由于c对象走的是Student的构造,没有直接走Person的构造.所以name=zsaa,没有给Person中的__name赋值,
                                # 这个name是Student中的name,不是Person中的__name,这两不是一个属性.所以即使c.eat()可以调用,但是
                                # 没给__name赋值，会导致报错.所以，要加上这一行
                                # 或者,把Person中的__name改成name,因为赋值了,所以能找到name这个值
        self.name = name
        self.grade = grade
    def study(self):
        print(f"{self.name} is studying...")

class ChineseStudent(YellowRace, Student):
    # def __init__(self, name):
    #     Person.__init__(self, name)
    #     # super(Student, self).__init__(name)
    #     """
    #     想直接调用Person的构造:
    #     1.Person.__init__(self, name),注意要加self;
    #     2.根据MRO,找到Person的上一个类,super(Student, self).__init__(name)
    #     此时创建对象,要求只有1个参数name,调用ChineseStudent的构造(而不是Student),进而调用Person构造
    #     """
    #     self.name = name
    country = "中国"

c = ChineseStudent("zsaa",100) # 调用的是Student的构造,会根据MRO从左到右按顺序寻找第一个有构造的类
# c.study()
# c.eat()
# print(c.country)



# ----MRO：方法解析顺序----
print(ChineseStudent.__mro__) # 打印出类的继承链,以此查看方法的解析顺序.
# (<class '__main__.ChineseStudent'>, <class '__main__.YellowRace'>, <class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
# super()不是简单的调用父类,而是基于当前类的MRO,调用下一个类.比如YellowRace的super()就是Student类,而不是Person
# 调用构造时,MRO 从前往后找构造方法，找到第一个存在该方法的类就停止。比如YellowRace有构造,那就停止,另外创建对象时必须按照YellowRace构造的参数,不能多

class GrandParent:
    def __init__(self):
        print("Initializing GrandParent")


class Parent1(GrandParent):
    def __init__(self):
        super().__init__()  # 方式2：父类也用 super()
        print("Initializing Parent1")


class Parent2(GrandParent):
    def __init__(self):
        super().__init__()  # 方式2：父类也用 super()
        print("Initializing Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        # Parent1.__init__(self)
        # Parent2.__init__(self)
        super().__init__() # 可避免重复调用
print(Child.__mro__)
Child()
