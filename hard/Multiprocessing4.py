import multiprocessing
import random
import time


# 间隔随机时间向queue中放入随机数
def func1(queue):
    while True:
        queue.put(random.randint(1, 50))
        time.sleep(0.1)

# 从queue中取出数据
def func2(queue):
    while True:
       print("="* queue.get())

# ---- 进程池之间使用Manager().Queue----
if __name__ == "__main__":
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(processes=2)
    res1 = pool.apply_async(func1, args=(queue,))
    res2 = pool.apply_async(func2, args=(queue,))
    pool.close()
    pool.join()




# multiprocessing.Queue(): 原生IPC队列,只能给普通Process进程用,不能传给进程池Pool,底层是操作系统管道实现,性能更好
# multiprocessing.Manager().Queue(): 由Manager管理进程托管的队列,支持普通Process+进程池Pool,底层走网络socket通信,性能更低
# Queue管道,主要作用: 底层封装了管道,多进程之间传递消息数据;一个进程将数据放入队列,另一个进程取出数据,数据一旦被get,队列中不再保留,只能消费一次