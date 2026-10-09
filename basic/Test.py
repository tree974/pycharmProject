# ---- 注释 ----
# 单行注释
"""
多行注释，但不能嵌套
"""
print("""这是字符串,不是注释""")


# ---- 变量 ----
var1 =2
var2 = 3
result = var1 + var2
print(result)
name = "张三"
age = 18

# 多个变量的创建
var1 = var2 = var3 = 4
var4,var5,var6 = 1,2,3
print(var1,var2,var3)
print(var4,var5,var6)
var4,var5 = var5,var4
print(var4,var5,var6)
print(f"var1的值: {var1}")

#  ---- 标识符 ----
"""
命名规则: 
只能包含字母、数字和下划线，且不能以数字开头
区分大小写，即Name和name是两个不同的标识符
不要和关键字重复
"""
Name = "张三"
name = "李四"
print(Name, name)

# python的标准库提供了keyword模块,可以通过keyword模块输出所有关键字
# import keyword
# print(keyword.kwlist)
# 或者
from keyword import kwlist
print(kwlist)

# ---- 常量 ----
# 没有特别约束,一般用大写表示,后面最好不要修改值
PI = 3.14
print(PI)





