# 互斥锁:解决线程之间共享数据存在的线程安全问题
import time
import threading

def func():
    global g_num # 告诉 Python，下面代码里的g_num，去全局作用域找，不要在函数内新建局部变量
    for _ in range(10): # _:普通变量名,当下面代码不会用到时,可以使用_
        tmp = g_num + 1
        time.sleep(0.1) # 由于多线程中共享数据存在线程安全问题,线程1还没执行到下面这行,线程2又开始被轮询到了,
        # 所以,如果不加这一行,操作时间太短,没办法暴露问题,可能是正确结果;加了这一行后,可能结果就变小了
        g_num = tmp
        print(f"{threading.current_thread().name}: {g_num}\n", end="")

if __name__ == '__main__':
    g_num = 0 # 全局变量,代码中用到的任意地方的值都是一样的
    threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)] # 列表推导式
    [t.start() for t in threads] # 等价与: t.start(); t1.start(); t2.start()
    [t.join() for t in threads]
    print(g_num)

# 互斥锁:某个线程要更改共享数据时,先将其锁定,其他线程不能更改.直到该线程释放资源,其他线程才能再次锁定该资源
# 保证了每次只有一个线程进行写入操作,从而保证多线程下数据的正确性
def func1():
    global g_num
    for _ in range(10):
        lock.acquire(blocking=True) #获取锁,当blocking=True,线程B一直等待线程A释放锁,=False,如果还在上锁,那么放弃本次操作,不执行下面的逻辑
        tmp = g_num + 1
        time.sleep(0.1)
        g_num = tmp
        lock.release() # 释放锁
        print(f"{threading.current_thread().name}: {g_num}\n", end="")
if __name__ == '__main__':
    g_num = 0
    lock = threading.Lock() # 创建锁
    threads = [threading.Thread(target=func1,name=f"线程{i}") for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(g_num)