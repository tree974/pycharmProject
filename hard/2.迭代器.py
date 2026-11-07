# ----迭代器: 迭代-遍历容器的一种方式; 注意是遍历容器  ----
"""
1.可迭代对象Iterable：可直接作用于for循环的数据类型: (这些类型生成的对象就叫做迭代器对象Iterable)
    容器: list、tuple、dict、set、str
    注意: 可迭代对象本身不一定能next(), 需要用iter()拿到迭代器
2.迭代器Iterator: 可记住当前遍历位置的工具(当前遍历到哪儿了),取完就没了.必须有__next__和__iter__
3.生成器Generator: 一种特殊的迭代器,包括①生成器和②带 yield 的generator function。优点是避免一次性生成大量数据增加内存,而逐步产生值
生成器 ⊂ 迭代器 ⊂ 可迭代对象 (所有迭代器都是可迭代对象,反之不成立,生成器属于迭代器)

可迭代对象需要先iter(),再next();
迭代器和生成器: 可直接next()
"""



# ----带yield的generator function,调用后返回值是一个迭代器对象----
def gen_func(): # 带yield的函数,本身不是一个迭代器对象,而调用后才会生成一个迭代器
    yield 1 # yield：暂停函数,会把1返回,并且保存当前所有变量状态,等下次再调用next,就从当前位置向下执行
    yield 2
    yield 3

# 调用函数,得到generator[生成器对象]
g = gen_func() # 带`yield`的函数，是「生成器函数」：调用它的时候，不会执行函数体内代码，只会创建并返回一个生成器对象
print(type(g)) # <class 'generator'>
# 生成器对象可以直接for循环
for item in g:
    print(item)

# ---- 生成器表达式 ----
g = (i for i in range(10))
print(f"生成器表达式: {next(g)}") # 0
print(f"生成器表达式: {next(g)}") # 1

# ----可迭代对象转为迭代器----
list = [1,2,3] # 列表: 可迭代对象
# next(list) # 直接报错,列表不是迭代器,不能直接next ('list' object is not an iterator)
it = iter(list)  # 从可迭代对象,生成迭代器
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # 抛出StopIteration,代表取完了

# ---- 手写迭代器 ----
class MyIterator:
    def __init__(self):
        self.n = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 3:
            raise StopIteration
        res = self.n
        self.n +=1
        return res
# it = MyIterator()
# for i in it: # for循环底层逻辑: 会自动调用iter(可迭代对象)拿到迭代器,然后不断调用next(),直到捕获到StopIteration结束
#     print(i)
# 上面的for循环完全等价于下面的代码
it = MyIterator()
obj = iter(it) # 等价调用__iter__()
while True:
    try:
        i = next(obj) # 等价调用__next__()
        print(i)
    except StopIteration:
        break






# -----判断是否是可迭代对象 -----
from collections.abc import Iterable
print(isinstance([], Iterable))    # 列表
print(isinstance((), Iterable))    # 元组
print(isinstance(set(), Iterable)) # 集合
print(isinstance({}, Iterable))    # 字典
print(isinstance("100", Iterable)) # 字符串
print(isinstance(100, Iterable))   # 数字


# -----判断是否是迭代器 ----
from collections.abc import Iterator
print(isinstance([], Iterator))    # 列表
print(isinstance((), Iterator))    # 元组
print(isinstance(set(), Iterator)) # 集合
print(isinstance({}, Iterator))    # 字典
print(isinstance("100", Iterator)) # 字符串
print(isinstance(100, Iterator))   # 数字
print(isinstance((x for x in range(10)), Iterator))   # True



# ---- 使用函数创建生成器 ----
def fibo(): # 斐波拉契数列
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
f = fibo() # 带有yield的函数,调用函数只是创建生成器对象,不会立即执行函数代码,只有next才会执行函数代码
print(next(f))
print(next(f))
print(next(f))

def fibo(n):
    a,b, counter = 0,1,0
    while counter < n:
        yield b
        a,b,counter = b, a+b, counter+1 # 1 1 1; 1 2 2;2 3 3;3 5 4
    return "aaaaa" # 如果要获取生成器中return的值,需要捕获StopIteration异常
f = fibo(5)
try:
    while True:
        print(next(f)) # 1 1 2 3 5
except StopIteration as result:
    print("StopIteration",result) # StopIteration aaaaa


# ----send():恢复执行并向生成器函数发送一个值,这个值作为yield表达式的结果----
def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'
    while True:
        # task_id为0,则int_value+1
        # task_id为1,则char_value+1
        match task_id:
            case 0:
                task_id = yield int_value # 返回int_value,并接收send()发过来的值给task_id
                int_value += 1
            case 1:
                task_id = yield char_value # 返回char_value,并接收send...
                char_value = chr(ord(char_value) + 1)
            case _:
                task_id = yield # 返回None
g = gen()
print(next(g)) # 0,此时函数暂停,返回yield的值0;`next(g)` 等价于 `g.send(None)`
print(g.send(1)) # A,此时send函数发过来的值给了task_id=1,再执行int_value+1=1,再次循环,返回yield=A
print(g.send(0)) # 1,task_id=0,char_value=B,再循环,返回yield=1
print(g.send(1)) # task_id=1,int_value=2,再次循环,返回yield=B