import re

class Customer1:
    def __init__(self,c_id,name,age,phone,email):
        self.id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    # 判断这些字段是否合法
    @staticmethod
    def check_id(self, c_id):
        return c_id.isdigit()

    @staticmethod
    def check_name(self, name):
        return name.isalpha()

    @staticmethod
    def check_age(self, age):
        return age.isdigit()

    @staticmethod
    def check_phone(self, phone):
        return True if re.match(r"^1[345789]\d{9}]$", phone) else False # 一共11位数,其中第一位是1,第二位是[]中的这几个数,然后后面跟着9个数字

    @staticmethod
    def check_email(self, email):
        pattern = r"[\w!#]"
        return True if re.match(pattern, email) else False
