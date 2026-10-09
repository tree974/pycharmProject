# 这是一个示例 Python 脚本。
import sys


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
"""
这是注释文字
"""



# 全局导入包 import 包名.模块名 [as 别名]
# 最后一项可以是包名或者模块名,如果是包名,必须在__init__.py文件中指定导入包的哪些模块,避免导入太多

import graphic.circle # 引入包本身,你可以写`graphic.circle.xxx`,调用的时候把包名带上.另外,这里必须要导入具体的子模块,才能使用,也可以在__init__.py中导入
print(graphic.circle.area(10))
print(sys.path)

# from graphic import * # 取出包里的所有成员导入,不会自动创建包名这个变量
# print(circle.area(10))


