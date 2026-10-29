# ---- 封装 ----
# 私有化:为了限制属性和方法只能在类内访问,外部无法访问; 或父类中某些属性和方法不希望被子类继承
#   单下划线: 非公开API,_var1
#   双下划线: 表示私有方法和属性,有2个前缀下划线,并至多一个后缀下划线,如__x,会被改写为_类名__x。
#       ①类内可以通过__x访问;②其他地方只能通过_类名__x访问

# @property:
#   ①将方法变为属性: 用在普通方法上,即可将方法转为属性,对象.方法名调用,不用加();
#   ②如果是私有属性__name,用在属性名方法上(不加__),此时私有属性变成了只读属性;只有加上属性名.@setter时,才可以写
#   ③用property修饰的方法,不要和变量重名,否则会无限循环
class Person:
    def __init__(self, name):
        self.__name = name   # name是私有属性
    def get_name(self):
        return self.__name  # 私有属性可通过类内 __name访问
    def __private_method(self): # 私有方法和私有属性都用__表示
        print("这是一个私有方法")

    @property   # 可将方法eat转为属性eat
    def eat(self):
        print(f"{self.__name} is eating...")
    @property
    def name(self): # 将方法名设置为去掉双下划线的私有属性名称,就变成了只读属性?但私有属性本身怎么修改呢
        return self.__name # 变成了只读属性,p.name = '李四'报错
    # @name.setter
    # def name(self, new_name):
    #     self.__name = new_name # 变成了读写属性,可通过p.name = '李四'

p = Person("张三")
# 访问私有属性的两种方式:
print(p.get_name())     # ①调用类方法,类方法中通过__属性名访问;
print(p._Person__name)  # ②类外通过 _类__name访问
# print(p.__name)       # 报错
# print(p.__private_method())# 报错
p._Person__private_method()# 私有方法可通过类外 _类__方法名访问

# 使用@Property
p.eat    # 该方法变成了属性,直接调用属性即可
print(p.name) # name方法上加了@Property,就相当于直接调用的p.name()
"""
p.name = "abc"详解:
当调用name这个属性时:
1.系统会先去寻找类里面是否有这个描述符
    ①如果没有,那么就表示这个name是一个动态新增的属性,可以直接赋值;
    ②如果有,那么分两种情况:
        i.这个name本身是实例属性,可以修改;
        ii.这个name是加了@Property的name()方法,那么此时就不能去修改,因为@Property只有__get__;
            只有当@name.setter再次作用在了name()方法上,就可以修改,因为设置了__set__

"""
p.name = "abc" # 注意:用@Property标记的方法,变成了私有属性,此时就不能修改了,除非加了属性名.@setter
print("修改name属性值: ",p.name)


