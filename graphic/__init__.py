# import graphic.circle # 如果其
import graphic # 如果其他文件需要import graphic,那么必须导入相关的子模块,因为__init__这里只导入了graphic,默认不会自动加载子模块
__all__ = ["circle"]   #__all__只适用于from x import *,导入所有模块的时候会限制
# 另外,如果是包级别的__init__.py,这个最小粒度是模块级别,里面的方法不能写这里
# 但如果是模块级别,这个里面可以是方法以及模块内的任何成员
