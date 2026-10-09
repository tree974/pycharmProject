import re
class Customer:
    """客户类"""
    def __init__(self, c_id, name, age="None", phone="None", email="None"):
        """初始化客户信息"""
        self.id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod # 该方法属于类本身,不属于实例对象,调用时不需要创建对象,也不用传self
    def check_id(c_id):
        """检查id格式"""
        # 检查客户id是否为纯数字
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        """检查name格式"""
        # 检查客户姓名是否为字符
        return name.isalpha()

    @staticmethod
    def check_age(age):
        """检查age格式"""
        # 检查客户年龄是否为整数
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        """检查phone格式"""
        # 检查客户电话是否合法
        return True if re.match(r"^1[345789]\d{9}]$", phone) else False # python正则前面的r: 原始字符串,关闭python里反斜杠\的转义功能
        # 就比如这个地方的r,如果不写r,就需要\\d
        # 另外,正则表达式的开始^和结尾$,如果要校验整个输入,首尾加上;但如果只是查找/匹配/提取片段,不要加上

    @staticmethod
    def check_email(email):
        """检查email格式"""
        # 检查客户邮箱是否合法
        pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^{|}~.]+\.[a-zA-Z{2,}$]"
        return True if re.match(pattern, email) else False

    def __str__(self):
        """打印客户信息"""
        return (f"Id: {self.id:<5}, Name: {self.name:<10}, Age: {self.age:<5}, Phone: {self.phone:<15}"
                f", Email: {self.email:<25} ") # 多对引号拼接的字符串,每段引号前面都要加上f; 或者换成3引号方式"""""",前面只加一个f即可(但这种方式会保留换行符,打印出来也会存在换行符)
        # return (f"""Id: {self.id:<5}, Name: {self.name:<10}, Age: {self.age:<5}, Phone: {self.phone:<15}
        #         , Email: {self.email:<25} """)

