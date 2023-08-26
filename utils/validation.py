import re

class Validation:
    @staticmethod
    def validate_email(email):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_password(password):
        # 密码至少包含一个大写字母，一个小写字母和一个数字，且长度在8到20之间
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$'
        return re.match(password_regex, password) is not None