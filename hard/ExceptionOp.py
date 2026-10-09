# 异常处理
# 1.try except
try:
    result = 3/0
    print("没有发生异常1")
except ZeroDivisionError as e:
    # raise e # 抛出异常
    print(e)
else:   # 其实和放在try中是一样的效果
    print("没有发生异常2")
finally: # 和放在try except之外效果是一样的
    print("无论是否异常都会执行")
print("继续")

def int_add(x,y):
    assert isinstance(x,int) and isinstance(y,int),"参数类型异常"
    return x+y
print(int_add(3,4))
# int_add("1","2") # AssertionError: 参数类型错误

# 若内层异常不能处理,则交给外层,直到能处理的那层
try:
    try:
        try:
            a = 1/0 # 这个异常是ZeroDivisionError
        except NameError as e:
            print("第三层", type(e), e)
    except TypeError as e:
        print("第二层", type(e), e)
except Exception as e:
    print("第一层",type(e),e)

