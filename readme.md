从git上拉取项目后：
`python -m venv venv` 创建环境
然后重启pycharm,会自动配置解释器,并自动安装依赖
# `pip install -r requirements.txt` 安装依赖
pip freeze > requirements.txt 将需要的依赖信息放到文件中
git 提交：代码 + `.gitignore` + `requirements.txt`