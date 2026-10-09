# 进程池
"""
multiprocessing.Pool([processes[,initializer[,initargs[,maxtasksperchild[,context]]]]])
"""
import os
import time
import multiprocessing

# 打印10个数字,每个间隔1s
def func():
    for i in range(10):
        print(os.getpid(), i)
        time.sleep(0.5)

if __name__ == "__main__":
    # 指定进程池大小
    process_num = 5
    pool = multiprocessing.Pool(process_num)
    for p in range(process_num):
        # 阻塞式
        # pool.apply(func) # 每个进程都会打印10个数字,每隔0.5s,而且是按顺序执行的,当第一个进程打印完后,才会开始第二个进程打印
        # 2240(第一个进程id) 0 2240 1 2240 2.... 2240 9
        # 非阻塞式
        pool.apply_async(func) # 每个进程也会打印10个数字,但是每打印1个数字,都是5个进程按顺序打印,而不是等第一个进程打印完10个后第二个进程才开始打印
        # 28100(第一个进程id) 0 18064(第二个进程id) 0 .... 28100(第一个进程id) 9 18064(第二个进程id) 9
    pool.close()  # 告诉进程池,不再接收新认为
    pool.join()   # 阻塞主进程,等待进程池中所有子任务执行结束,才继续执行主进程.必须close()在前搭配
    print("end") # 如果上面close和join都不加,那么再使用非阻塞式的时,就会立即打印end,然后整个主进程结束