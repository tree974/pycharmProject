__all__ = ["num","add"] # 内容必须要用引号引起来

num = 100
num1 = 200
_str1="abc"
def add(a, b):
    return a+b

if __name__ == "__main__": # 不加这一行,只要导入这个模块,下面这个打印就会执行.加了后,不会执行,只有本类可以执行
    print(add(num, num1))