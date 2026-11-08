# 自定义Thread子类创建线程
import time
import threading

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        flag =0
        while True:
            print(f"{self.name}:{str(flag)*5}")
            flag = flag ^ 1
            time.sleep(0.1)

if __name__ == '__main__':
    t1 = Worker("线程1")
    t2 = Worker("线程2")
    t1.start()
    t2.start()