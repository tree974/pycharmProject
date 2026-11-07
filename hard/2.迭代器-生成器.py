"""
生成器: 特殊的迭代器
返回数据时,搭配yield使用,暂停后面的数据返回,按需返回.可节省内存

"""
# 1.使用推导式创建生成器
gen = (i for i in range(5)) # 注意:这个()不是元组推导式,python中没有元组推导式;
"""
[]:列表推导式->list
{x for ...}:集合推导式->set
{k,v for ...}:字典推导式->dict
():生成器表达式->generator
"""
print(gen) # <generator object <genexpr> at 0x000002416F9A97D0> 生成器对象
for x in gen:
    print(f"{x}", end=",")
print()

# 2.使用函数创建生成器
def fibo():
    a, b = 0, 1
    count = 1
    while count < 5:
        yield b
        a, b = b, a+b
        count += 1
    return "done"
f = fibo() # fibo中含有yield,所以调用后不会立即执行,而是返回生成器对象
try:
    while True:
        print(next(f)) # 生成器可直接next,而可迭代对象必须先使用iter()拿到迭代器,再next
except StopIteration as e:
    print(f"StopIteration: {e}") # 获取生成器函数返回值,要捕获StopIteration异常


print("send方法向生成器发送值...")
def gen():
    task_id = 0
    a = 0
    c = "A"
    while True:
        match task_id:
            case 0:
                task_id = yield a
                a += 1
            case 1:
                task_id = yield c
                c += "a"
            case _:
                task_id = yield # 返回None
g = gen() # 函数带有yield,所以返回的是生成器对象
# print(next(g)) # 首次task_id默认值是0
print(g.send(None)) # 这个也是启动生成器的,参数为None;等价于next(g)
print(g.send(1)) # A.恢复yield暂停,开始执行;并向生成器函数发送一个值,然后返回生成器产生的下一个值
print(g.send(0)) # 1
print(g.send(1)) # Aa
