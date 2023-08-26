from flask import Blueprint, render_template, request
from models.user import User

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 处理用户登录请求
        username = request.form['username']
        password = request.form['password']
        user = User(username, '', password)
        user.login()
        # 其他处理逻辑
    return render_template('user/login.html')

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 处理用户注册请求
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username, email, password)
        user.register()
        # 其他处理逻辑
    return render_template('user/register.html')

@user_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # 处理更新用户信息请求
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username, email, password)
        user.update_profile()
        # 其他处理逻辑
    return render_template('user/profile.html')