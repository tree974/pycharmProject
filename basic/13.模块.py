__all__ = ["num","add"] # 内容必须要用引号引起来,表示该模块哪些成员可以被其他模块导入(只针对使用 from import * 导入模块时有效)

num = 100
num1 = 200
_str1="abc"
def add(a, b):
    return a+b

class A():
    def __init__(self, a):
        self.a = a
    def add(self, b):
        return self.a + b
if __name__ == "__main__": # 不加这一行,只要导入这个模块,下面这个打印就会执行.加了后,不会执行,只有本类可以执行
    print(add(num, num1))
    a = A(num)
    print(dir(a))
# import sys
# print(sys.path)