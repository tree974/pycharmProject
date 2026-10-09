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
match month := 3: # :=可以直接把值赋给变量,并且赋值后还能把值返回出来,多用于循环、条件判断里面
    case 1 | 2: # |是专门用于模式匹配的操作符,能把多个常量或者模式组合起来,实现"或",不能使用or
        print("这是1月份或者2月份")
    case _:
        print("这不是1月份")

# 三目运算符
num1 = 2
num2 = 3
max_num = num1 if num1 > num2 else num2
print(max_num)

# while循环
# 第一周有2只兔子,此后每周兔子的数量都增加上周数量的两倍,求第10周共有多少兔子
rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week = week + 1
    if week == 3:
        break
else: # 如果有break,那么通过break终止后,else里的语句就不会再执行了;没有break时,就会执行else语句; 下面的for循环也一样
    print(f"第10周共有{rabbit}只兔子")

# for循环
sum = 0
for i in [1,2,3,4]:
    print(i)
    sum = sum + i
    if i == 3:
        break
else:
    print(f"for循环结束,sum={sum}")

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