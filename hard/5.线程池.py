# 线程池
# ThreadPoolExecutor是concurrent.futures模块中的线程池实现,运行提交任务到线程池,并管理任务的执行和结果
# concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix="", initargs=None)

# 3个线程,每个线程都将字符列表中的每个字符与1异或
import concurrent.futures
def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end= "")
    return word

if __name__ == '__main__':
    word = list("abcdef")
    # 使用with语句来确保线程被快速清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")

    print("".join(word))

