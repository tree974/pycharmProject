# 线程
"""
1. 线程是处理器任务调度和执行的基本单位
2. 一个进程至少有1个线程,也可以运行多个线程
3. 多个线程间可共享数据
4. 多线程指在同一进程中同时执行多个任务
"""
import threading

# python库中提供2个模块,__thread和threading(高级模块,对__thread进行了封装)
# threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, * ,daemon=None)

# 两线程分别交替打印
import time
import threading
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f"flag" * 5) # 源码一行代码，都不代表原子操作，操作系统随时可以发生线程切换.
        # 所以,可能会出现 线程2线程1  flagflagflagflagflagflagflagflagflagflag 这样的打印
        flag = flag ^ 1
        time.sleep(0.5)

if __name__ == '__main__':
    t1 = threading.Thread(target=func, name="线程1")
    t2 = threading.Thread(target=func, name="线程2")
    t1.start()
    t2.start()