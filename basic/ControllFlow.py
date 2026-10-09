# 从random模块中导入randint函数
from random import randint
balace = randint(1,30)
print(f"余额： {balace =}")
price = 20
if (balace > price):
    print("余额足够")
elif (balace < price):
    print("余额不足")
else:
    print("余额刚好够")


# match case语法
# month = 2
match month := 2: # :=可以直接把值赋给变量,并且赋值后还能把值返回出来,多用于循环、条件判断里面
    case 1:
        print("这是1月份")
    case _:
        print("这不是1月份")

# 三目运算符
num1 = 2
num2 = 3
max_num = num1 if num1 > num2 else num2
print(max_num)

# for循环
for i in [1,2,3,4]:
    print(i)

for i in "hello world":
    print(i)

for i in range(10):
    print(i)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()

# pass 占位符,是空语句,是为了保持结构完整性
for i in range(1,10):
    pass