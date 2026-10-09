# from distutils.core import setup
#
# setup(
#     name = "graphic", # 需要打包的名字
#     version = "1.0", # 版本
#     py_modules = ["graphic.circle", "graphic.rectangle"] # 需要打包的模块
# )

# python setup.py build->构建,生成build临时目录(编译、拷贝源码)
# python setup.py install->安装,把build里面的包安装到当前python环境,安装完后就可以import graphic
# python setup.py sdist -> 生成源码压缩包.tar.gz
# python setup.py bdist_wheel -> 生成whl安装包(推荐,别人pip安装用这个)

# build: 工厂把零件整理、组装成半成品
# install：把半成品安装到自己的机器,pycharm中还是需要点击+号后,然后安装
# sdist/dbist_wheel: 打包成成品安装包给别人
from setuptools import setup, find_packages

setup(
    name="graphic",
    version="1.0",
    packages=find_packages(), #自动扫描所有带__init__.py的包，graphic会被识别,要把目录打包进去,就需要加上__init__.py
    py_modules=["main"], # 打包根目录下面的单个python文件
    package_data={"graphic":["static/*"]}, # 打包静态资源文件-不能打包根目录下的文件,只能打包包目录下的静态文件
    # 如果要打包根目录下的文件,需要使用到MANIFEST.in这个文件,但是注意:这种方式只能用在打包sdist(即打成tar.gz包时生效)
    include_package_data=True # 读取MANIFEST.in
)