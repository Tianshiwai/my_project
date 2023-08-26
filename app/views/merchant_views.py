from flask import Blueprint, render_template, request
from models.merchant import Merchant

merchant_blueprint = Blueprint('merchant', __name__)

@merchant_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 处理商家登录请求
        name = request.form['name']
        password = request.form['password']
        merchant = Merchant(name, '', password)
        merchant.login()
        # 其他处理逻辑
    return render_template('merchant/login.html')

@merchant_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 处理商家注册请求
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        merchant = Merchant(name, email, password)
        merchant.register()
        # 其他处理逻辑
    return render_template('merchant/register.html')

@merchant_blueprint.route('/dashboard')
def dashboard():
    # 处理商家仪表盘请求
    # 其他处理逻辑
    return render_template('merchant/dashboard.html')