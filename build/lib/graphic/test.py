# 相对导入
import sys

# from .circle import area   # 相对导入,会将本项目作为顶层脚本,不再认为它属于哪个包,所以.找不到路径
# print(sys.path)
from graphic.circle import area
print(sys.path)
print(area)

print(dir(area))
print(sys.path)