# import multiprocessing
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs=(), * ,daemon=None).start()
# group: 应当始终为None,它的存在是为了与threading.Thread兼容
# target: 由run()方法来发起调用的可调用对象,默认为None
# name: 进程名称,默认为None则自动分配
# args: 针对目标调用的参数元组
# kwargs: 针对目标调用的关键字参数字典
# daemon: 是否为守护进程，True活False,默认为None则继承父进程


import time
import multiprocessing
# 向文件中写入数据
def write_file():
    with open("test.txt", "a") as f:
        while True:
            f.write("hello world\n")
            f.flush()
            time.sleep(0.5)
# 从文件中读取数据
def read_file():
    with open("test.txt", "r") as f:
        while True:
            time.sleep(0.5)
            print(f.read(1))

# 在Windows下运行 multiprocessing 代码，如果不加 `if __name__ == "__main__":`，会疯狂递归创建进程，直接报错崩溃！
if __name__ == "__main__": # 当前文件只有直接执行的时候,才会允许这里面的代码;如果是被import的,就不会执行
    # 创建一个子进程用于写文件
    p1 = multiprocessing.Process(target=write_file)
    # 创建一个子进程用于读文件
    p2 = multiprocessing.Process(target=read_file)
    p1.start()
    p2.start()


