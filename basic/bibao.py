# 闭包: 内层函数,携带外层函数的变量环境,外层函数执行完后,依然能访问外层的局部变量
"""
闭包的3个条件:
1.有嵌套函数
2.内层函数使用外层函数的变量(非全局变量)
3.外层函数返回内层函数(注意只是返回内层函数对象,而不是调用,也就是没有最后的())
"""
def outer(x):
    # 外层变量x
    def inner():
        print(x) # 内层函数使用外层的变量x
    return inner # 返回内层函数对象,不是调用

f = outer(100)
# outer函数此时已经执行完毕,理论上函数局部变量应该销毁
f() # 输出100,依然能拿到100,这就是闭包


# 非闭包,普通函数调用
def outer(x):
    def inner():
        print(x)
    inner() #直接调用了inner,而不是返回对象
    # outer结束后,没有谁再使用x了,x直接销毁

outer(200) # outer结束后,拿不到inner,x直接被回收,没有闭包



# 闭包测试1
def outer(num):
    def inner():
        print(num)
    return inner

f1 = outer(10)
f2 = outer(20)

f1() # 输出？ 10
f2() # 输出？ 20

# 闭包测试2
funcs = []
for i in range(3):
    def inner():
        print(i) # 注意,这个i每次都会变化,所以最后实际上i=2
    funcs.append(inner)

funcs[0]()  # 2
funcs[1]()  # 2
funcs[2]()  # 2

# 闭包测试3
funcs = []
for i in range(3):
    def inner(n=i): # 默认参数在定义函数那一刻就固定值
        print(n)        # 固定值后,i的改变实际不会影响n了;比如当i=2时,n=2,inner()是当时的值,而不是最后的变量值,当n=2时,i一定=2,而不=3
    funcs.append(inner)

funcs[0]() #0
funcs[1]() #1
funcs[2]() #2
