class Person:

    def __init__(self, age, name=None): # 构造方法
        self.__age = age # 私有属性
        self.name = name

    def eat(self): # 普通方法
        print(f"父类{self.name}在吃饭")

    def __drink(self): # 私有方法
        print(f"父类{self.name}在喝酒")

    def __run(self): # 私有方法,子类覆写
        print(f"父类{self.name}在跑步")

    @property
    def age(self):       # 对外提供接口调用私有属性
        return self.__age

    def get_drink(self): # 对外提供接口调用私有方法
        return self.__drink()

    @property
    def run(self):
        return self.__run()

class YellowRace(Person):
    def __init__(self, age, name=None):
        super().__init__(age, name)

    def __run(self): # 子类覆写父类的私有方法
        print(f"子类{self.name}在跑步")

    @property
    def run(self):
        return super().run # run是属性,不是方法,所以不能加()

    def test(self):
        # print(f"父类的私有属性: {self.__age}") # 如果是这样写,不是去访问的父类,而是子类(_YellowRace__age)
        # self.__drink() # _YellowRace__drink
        # print(f"父类的私有属性: {self._Person__age}") # 访问父类,需要显式调用
        # self._Person__drink() # 访问父类,需要显式调用
        # 但是显式调用违背了封装原则,__的初衷就是一个类中私有的,子类和外部都不能访问.
        # 所以,通过@Property标记私有属性方法,来对外提供访问私有属性的接口
        print(f"父类的私有属性: {self.age}") # 由于子类没有这个属性,所以调用的是父类
        self.get_drink() # 由于子类没有这个方法,所以调用的是父类
        self.__run() # 这是直接调用的子类本身的方法
        self.run # 这是通过@property定义的run方法,此时就是属性run,而不是方法run,所以不用加();然后调用的父类run方法,进而获取父类__run私有方法

y = YellowRace(10,"张三")
y.test()