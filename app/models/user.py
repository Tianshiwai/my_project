class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def login(self):
        # 用户登录逻辑
        pass

    def register(self):
        # 用户注册逻辑
        pass

    def update_profile(self, **kwargs):
        # 更新用户信息逻辑
        pass

    def delete_account(self):
        # 删除用户账户逻辑
        pass