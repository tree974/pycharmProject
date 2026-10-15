# ----求一个整数n的阶乘----
# 非递归方式
def get_factorial(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
print(get_factorial(5))

# 递归方式
def get_factorial(n):
    return n * get_factorial(n-1) if n > 1 else 1 # 如果n>1,执行前面的表达式;
print(get_factorial(5))

