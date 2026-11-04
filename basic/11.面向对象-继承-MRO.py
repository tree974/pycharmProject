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
        # Parent2.__init__(self)
        Parent1.__init__(self) # 虽然这里是普通函数调用,但是Parent1里面的super仍然会遵守MRO
        # super().__init__() # 可避免重复调用
print(Child.__mro__)
print(Parent1.__mro__)
print(Parent2.__mro__)
Child()

# 注意: 只要是super()会沿着MRO链去找.
# 比如: Child的MRO: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.GrandParent'>, <class 'object'>)
# 那么Child的__init__中Parent2.__init__(self): 调用的就是GrandParent和Parent2
# 那么Child的__init__中Parent1.__init__(self): 调用的就是GrandParent和Parent2、Parent1
