# -------- 输入和输出 --------
input_str = input('请输入: ') # 输入的类型,都会转为字符串变量
print('input_str数据类型为: ', type(input_str), end='123\n') # print输出,end=表示用什么结尾

# 格式化输出
int1 = 10
float1 = 3.14
# java中的占位符和python中的区别: String s = String.format("name:%s, age:%d", name, age);
str1 = "int1 = %d, float1 = %f" % (int1, float1) # 中间的%格式化操作符,是把右边括号里的数据,依次填入左边模板中对应的%占位符
print(str1)
str2 = "int1 = {}, float1 = {}".format(int1, float1)
print(str2)
# 设置指定位置,按照位置填写
str3 = "int1 = {1}, float1 = {0}".format(float1, int1) #int1 = 10, float1 = 3.14
print(str3)
# 数字格式化
str4 = "{:*^20,.2f}".format(float1) # :后面添加多个参数对数字格式化
print(str4) # ********3.14********
# 使用大括号{}来转义大括号
print("{0}对应的位置是{0}".format("hello")) # hello对应的位置是hello,字符串中的数字是占位符
print("{}对应的位置是{{0}}".format("hello")) # hello对应的位置是{0},不带数字自动按顺序占位
# f-字符串,字符串前加一个f,字符串中的{}内写变量名
str5 = f"int1 = {int1}, float1 = {float1}"
print(str5) # int1 = 10, float1 = 3.14
# {}内变量后可以加上=,打印时会在变量值前加上 变量名=
str6 = f"{int1 = }, {float1 =}"
print(str6) # int1 = 10, float1 =3.14
# {}外再套一层{},即{{}}会转义
str7 = f"{{int1 = }}, {{float1 = }}"
print(str7) #{int1 = }, {float1 = }
str8 = f"{{888}}"
print(str8)
