# 闭包:
"""
1. 要有嵌套函数
2. 如果执行完外层函数,那么外层函数中的变量就不会再被访问,闭包的存在就是解决外层函数执行完毕后变量不能被访问的问题
3. 外层函数返回内层函数对象，而不是调用内层函数
"""
funcs = []
for i in range(3):
    def inner():
        print(i)
    funcs.append(inner)

funcs[0]()
funcs[1]()
funcs[2]()
