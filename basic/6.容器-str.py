# -------- 字符串:不可变的,有序的,字符串中元素不能修改 --------
str8 = 'abcd'
print(str8[:])  # abcd
print(str8[0])  # a
print(str8[0:2])# ab
print(str8[2:]) # cd
print(str8[:2]) # ab
print("ab" in str8) # 检查成员是否在字符串中
print("hello\nworld")  #转义字符串
print(r"hello\nworld") #原始字符串,加r不转义

str1 = 'abcdcecf'
print(str1.replace('a','x')) # xbcdcecf,字符串本身没有变
print(str1.split('c', 2)) # ['ab', 'd', 'ecf'],后边的数字表示切几次
print(str1.rsplit('c', 2)) # ['abcd', 'e', 'f'],从右边往左切,常用于文件名的提取,"data/log/2025/test.txt",print(path.rsplit('/',1))
print(type(str1.rsplit('c'))) # <class 'list'> list split后的类型还是list,python中没有原生数组类型

print("x".join(str1)) # axbxcxdxcxexcxf,将x元素作为分隔符,放到str1中
print(str1.strip('a')) #截取字符串两边的空格或指定字符
print(str1.lstrip()) # 截取左边的空格或字符
print(str1.rstrip()) # 截取右边的空格或字符

print(str1.removeprefix('a')) # bcdcecf 截取指定前缀
print(str1.removesuffix('cf')) # abcdce 截取指定后缀

# 大小写转换
str2 = "this_is_python"
print(str2.upper()) # THIS_IS_PYTHON
print(str2.lower()) # this_is_python
print(str2.swapcase()) # THIS_IS_PYTHON 反转大小写
print(str2.capitalize()) # This_is_python 将字符串第一个字母变为大写,其他字母变为小写
print(str2.title()) # This_Is_Python 将每个单词首字母大写.python中认定：一个新单词的开始=当前字符是字母,而且前一个字符不是字母

print(len(str2)) # 14
print(max(str2))
print(min(str2))

# 查找相关
print(str2.find('python')) # 返回第一个x的索引值,不存在则-1
print(str2.rfind('python'))
print(str2.index('python')) # 和find一样
print(str2.rindex('python'))
print(str2.count('t')) # 2, 返回x的个数
print(str2.startswith('th')) # True, 检查是否以x开头
print(str2.endswith('python')) # True

str3 = '  '
print(str3.isspace()) # True,检查字符串是否非空,且只包含空白,字符串长度必须大于0


str4 = 'abcd'
print(str4.center(10, '_')) #___abcd___,返回长度为10,且居中的字符串,默认空白用空格填充
print(str4.ljust(10,'_'))   #abcd______,左对齐
print(str4.rjust(10,'_'))   #______abcd,右对齐
print(str4.zfill(10))       #000000abcd,右对齐,空白用0填充

str5 = 'hello\r\nworld\r\nnihao' #\r\n和\n都可以
print(str5.splitlines()) # ['hello', 'world', 'nihao'],按行分隔字符串,将所有行字符串组成列表返回
str6 = 'helloworwld'
print(str6.partition('w')) # ('hello', 'w', 'orwld'),使用x将字符串分隔为3部分,不足3部分或没有x,则以空白填充
# str == 'helloorld' ('helloorld', '', '')
print(str6.rpartition('w')) # ('hellowor', 'w', 'ld')


str7 = 'hello\tworld'
print(str7.expandtabs(5)) # hello     world,将\t转为空格,同时指定每个\t空格数
str8 = '姓名:{name},年龄:{age}'
info = {"name": "zs", "age": 20}
print(str8.format_map(info)) # 姓名:zs,年龄:20,使用字典等映射关系数据来格式化字符串
str9 = 'abc123'
print(str9.isalnum()) # True,检查是否非空且只包含字母和汉字
print(str9.isalpha()) # False,检查字符串是否非空且只包含字母
print(str9.isdigit()) # False,检查是否非空且只包含阿拉伯数字0-9

str10 = 'ABCD'
print(str10.isupper()) # True,是否全是大写
print(str10.islower()) # False,是否全是小写
str11 = '一壹'
print(str11.isnumeric()) # True,检查是否非空且只包含数值字符,一、壹都认












