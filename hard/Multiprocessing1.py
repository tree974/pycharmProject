import os
import multiprocessing

# 自定义Process子类创建进程
class Worker(multiprocessing.Process):
    def run(self):
        print("进程id: ", os.getpid(), "\t父进程id:", os.getppid())

# 主进程,加载代码,定义Worker类,然后进入if __name__
if __name__ == "__main__":
    for i in range(5): # 循环重复,p=Worker()创建对象->p.start()创建子进程,自动执行run()
        p = Worker()
        p.start()