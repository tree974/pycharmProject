def printStar():
    row = 2
    while row > 0:
        print("*"*3)
        row -= 1

printStar()

def printIn(a,b,c):
    print(a+b+c)
printIn(a=1,b=2,c=3) #关键字传参

def printInfo(num, *args): # 不定长参数,一个*表示传入的是不定长元组
    print(num)
    print(*args)
printInfo(3,"a","b","c")

def printInfo1(num, **kwargs): # 两个**表示传入的是不定长字典
    print(num)
    print(kwargs)
printInfo1(3, key1=1, key2=2)

def func(a,b,c): # 通过*、**对列表、元组、字典解包传参
    return a+b+c
tuple1 = (1,2,3)
print(func(*tuple1))
dict1 = {"a":1, "b":2, "c":3} # 字典中的key必须和方法中参数名一致
print(func(**dict1))


# ---- 变量作用域 ----
"""
LEGB:
L-Local：函数局部变量
E-Enclosing: 外层嵌套函数变量(闭包外层)
G-Global: 全局变量
B-Built-in: 内建作用域,python解释器自带,类似max()、len()这些都是内建的,不用import
"""
#  global关键字: 将局部变量->全局变量
var1 = 10
def func():
    var1 += 2 # 在函数中修改变量,会默认把变量当成局部变量处理,那么就必须要初始化定义变量。所以,这里调用func会报错;
    # 但如果是可变变量,是可以修改的,依然会被当成全局变量,即使不加global
    print(var1)
# func()
print(var1)

def func2():
    global var1 # 函数内,加global,声明为全局变量,可修改值
    var1 += 2
    print(var1)
func2()
print(var1)

# nonlocal关键字:将内部函数作用域修改为外部函数作用域
def function_outer():
    var1 = 1
    print(var1)
    def function_inner():
        nonlocal var1 # 如果不加这一行,那么下面这一行是修改不了外部var1的,相当于下面的var1是内部函数局部变量,
        # 而外部var1只能用不能改;加了后,外部函数var1变成了200
        var1 = 200
        print(var1)
    function_inner()
    print(var1)
function_outer()



# ---- 匿名函数: 不用def来定义的函数,使用lambda定义 ----
# 不用匿名函数
def opeartor(a,b):
    return a+b
def func(a, b, opeartor):
    return opeartor(a,b)
print(func(1, 2, opeartor))

# 用匿名函数
print(func(1, 2, lambda a,b: a+b))


student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
print(sorted(student_list, key=lambda x: x["age"]))

map_result = map(lambda x: x * x, [0, 1, 3, 7, 9]) # map返回的也是迭代器
print(list(map_result)) # [0, 1, 9, 49, 81]


# ---- 函数的注释----
def dog(name:str, age:(1,99), species:'狗狗的品种') -> tuple: #返回值的注释用->
    return (name, age, species)
print(dog.__annotations__) #{'name': <class 'str'>, 'age': (1, 99), 'species': '狗狗的品种', 'return': <class 'tuple'>}
