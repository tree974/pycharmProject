# ---- 字典dictionary:无序键值对集合,{}定义,每个键值对之间用逗号分隔 ----
# 字典没有索引
dict1 = {}
dict2 = dict()
dict3 = {"name":"zs", "age":18}
dict4 = dict(name="zs", age=18)
dict5 = dict([("name","zs"),("age",18)])
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
squares = {x: x**2 for x in range(4)} # {0: 0, 1: 1, 2: 4, 3: 9}
print(squares)

dict1 = {"name": "Alice", "age": 18, "gender": "male"}
print(dict1["name"])
print(dict1.get("name","a")) # 不存在则返回默认值
dict1["address"] = "earth" # 添加元素
print("name" in dict1)
del dict1["address"]
# del dict1
# dict1.clear()


# 遍历字典
for x in dict1.keys(): # 通过key遍历
    print(f"{x}:{dict1[x]}", end="\t") # name:Alice	age:18	gender:male
print()
for x in dict1.values(): # 遍历value
    print(f"value={x}", end="\t")
print()
for x in dict1.items(): # 获取所有的(k,v),返回一个视图对象
    print(x)

# 其他方法
x = dict1.pop("name1", "test") # {'age': 18, 'gender': 'male'} 获取key对应的value(不存在,则使用默认值),同时删除该键值对
print(x) # test
print(dict1) # {'age': 18, 'gender': 'male'}
print(dict1.popitem()) # ('gender', 'male') 取出字典中最后一个键值对,如果为空则报错

dict2 = {"name": "zs", "age": 18}
x = dict2.setdefault("name1","test") # {'name': 'zs', 'age': 18, 'name1': 'test'},获取key对应value,如果不存在,则添加key;pop是删除,这个是添加
print(x) # test

dict3 = dict2.copy()
print(dict3)

list1 = ["name", "age"]
x = dict.fromkeys(list1, "test") # 以序列中元素做字典的key创建一个新的字典,可设置value的默认值
print(x)

