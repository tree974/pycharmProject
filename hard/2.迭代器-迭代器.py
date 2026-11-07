# 迭代器: 两个基本方法iter()和next()
# 创建迭代器
class Reverse:
    def __init__(self,value):
        self.value = value
        self.index = len(value) - 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        data = self.value[self.index]
        self.index -= 1
        return data

rev = Reverse([1,2,3,4,5])
print(rev) # <__main__.Reverse object at 0x00000225741C7F10>
iter(rev)
for char in rev:
    print(char)