# f = open("../static/file.txt", "w", encoding="utf-8")
# f.write("你好hello world")
# f.write("你好\n python")
# f.close()


f = open("../static/file.txt", "rt", encoding="utf-8")
# print(f.read(5)) # b:读取5个字节:b'hello'; t:读取5个字符:hello
# print(f.readline(2)) # 读取2个字符
# print(f.readline()) # 读取整行
# print(f.readline()) # 接着读
# list1 = f.readlines() # 读取所有内容,将每一行放入到列表中
# print(list1)

"""
print(f.read(5))
f.seek(0) # 移动偏移量并返回新的位置.seek是按字节,所以当参数>0时,在读取的时候要统一为字节(即rb模式)
print(f.read(1))
print(f.tell()) # 也是字节为单位,返回的当前光标所在的字节位置
"""

# f.truncate(3) # 从开头截断文件为3个字符.只能在w模式下执行
print(f.readable()) # True,是否可读
print(f.writable()) # False,是否可写
print(f.seekable()) # True,是否支持随机访问

import os
# os.rename("../static/1.txt", "../static/2.txt")
# os.remove("../static/2.txt") # 删除文件
# os.mkdir("../static/file") # 父级目录必须存在
# os.makedirs("../static/dir/file") # 即使父级目录不存在,也可以创建
# os.rmdir("../static/dir")
# os.removedirs("../static/dir")
# os.chdir("../static") # 进入指定目录
# print(os.listdir("../static"))

# print(os.path.abspath("../static/file.txt")) # 转为绝对路径
# print(os.path.basename("../static/file.txt")) # 获取文件名
# print(os.path.dirname("../static/file.txt"))
# print(os.path.getsize("../static/file.txt")) # 获取文件大小,字节
# print(os.path.exists("../static/file.txt"))
# print(os.path.isfile("../static/file.txt"))
# print(os.path.isdir("../static/file.txt"))
# print(os.path.getatime("../static/file.txt")) # 最后访问时间,时间戳
# print(os.path.getmtime("../static/file.txt")) # 最后修改时间,时间戳



# 递归遍历当前路径下所有目录和文件
# for root, dirs, files in os.walk(os.getcwd()): # os.walk: 遍历文件夹,递归,一层层往下找
#     print("当前路径: ", root)
#     print("目录: ", dirs)
#     print("文件: ", files)
#     print()


# 文件拷贝
def copyFile(source, target):
    source_file = open(source, "rb")
    content =  source_file.read()

    target_file = open(target, "wb")
    target_file.write(content)

    source_file.close()
    target_file.close()
copyFile("../static/file.txt","../static/file1.txt")
f.close()



