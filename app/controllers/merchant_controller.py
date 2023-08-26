from models.merchant import Merchant

def login():
    if request.method == 'POST':
        # 处理商家登录请求
        name = request.form['name']
        password = request.form['password']
        merchant = Merchant(name, '', password)
        merchant.login()
        # 其他处理逻辑

def register():
    if request.method == 'POST':
        # 处理商家注册请求
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        merchant = Merchant(name, email, password)
        merchant.register()
        # 其他处理逻辑

def dashboard():
    # 处理商家仪表盘请求
    pass
    # 其他处理逻辑