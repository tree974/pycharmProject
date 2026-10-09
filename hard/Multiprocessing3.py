# 进程间的通信
# 1. 不共享全局变量,比如子进程向传入的列表中添加元素,最终发现主进程与子进程之间的列表结果不同
# 进程间内存隔离,任何修改都是副本,互不影响(子进程间、子进程与主进程间)
import os
import multiprocessing

# 向list1中添加10个元素
def func(list1):
    for i in range(10):
        list1.append(i)
        print(os.getpid(),list1)

if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(os.getpid(),list1) # 15232 []




print("使用Queue通信....")
# 2.使用Queue通信:多个进程之间安全传递数据
# 返回一个使用一个管道和少量锁和信号量实现的共享队列(先进先出)实例.当一个进程将一个对象放进队列中时,一个写入线程会启动并将对象从
# 缓冲区写入管道中
import random
import time
# 间隔随机时间向queue中放入随机数
def func1(queue):
    for _ in range(5):
        num = random.randint(1, 50)
        queue.put(num)
        print(f"生产者放入数据: {num}")
        time.sleep(1)
        # 放入结束标记 None，告诉消费者：没有更多数据了
    queue.put(None)
    print("生产者：所有数据生产完成，发送结束信号")

# 从queue中取出数据
def func2(queue):
    while True:
        # 队列空就阻塞等待
        data = queue.get()
        # 读到 None，退出循环
        if data is None:
            print("消费者收到结束标记，退出")
            break
        print("=" * data)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=func1, args=(queue,))
    p2 = multiprocessing.Process(target=func2, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



