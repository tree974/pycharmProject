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
