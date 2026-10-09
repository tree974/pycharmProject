f = open("../static/file.txt", "w", encoding="utf-8")
f.write("hello world")
f.write("你好\n python")
f.close()



f = open("../static/file.txt", "rt")
print(f.read(5)) # b:读取5个字节:b'hello'; t:读取5个字符:hello
f.close()
