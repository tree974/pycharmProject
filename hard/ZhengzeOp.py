import re
test = [
    "13812345678",
    "11456817239"
]

pattern = r"^1[3456789]\d{9}$"
for i in test:
    print(f"{i:12}{"合法" if re.match(pattern,i) else "非法"}")