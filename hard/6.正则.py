import re
t = "abcdef123456"
print(re.search(r"\w+", t)) # r:字符串原样交给re,不用转义
print(re.search("\w+", t))

test = [
    "13812345678",
    "11456817239"
]

pattern = r"^1[3456789]\d{9}$"
for i in test:
    print(f"{i:12}{'合法' if re.match(pattern,i) else '非法'}")