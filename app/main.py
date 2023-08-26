# from flask import Flask, render_template

# app = Flask(__name__)

# # Home page
# @app.route("/")
# def home():
#     return render_template("index.html")

# # User routes
# @app.route("/user/login", methods=["GET", "POST"])
# def user_login():
#     # Handle user login logic
#     return render_template("user/login.html")

# @app.route("/user/register", methods=["GET", "POST"])
# def user_register():
#     # Handle user registration logic
#     return render_template("user/register.html")

# @app.route("/user/profile")
# def user_profile():
#     # Display user profile
#     return render_template("user/profile.html")

# # Merchant routes
# @app.route("/merchant/login", methods=["GET", "POST"])
# def merchant_login():
#     # Handle merchant login logic
#     return render_template("merchant/login.html")

# @app.route("/merchant/register", methods=["GET", "POST"])
# def merchant_register():
#     # Handle merchant registration logic
#     return render_template("merchant/register.html")

# @app.route("/merchant/dashboard")
# def merchant_dashboard():
#     # Display merchant dashboard
#     return render_template("merchant/dashboard.html")

# @app.route("/merchant/menu")
# def merchant_menu():
#     # Display merchant menu
#     return render_template("merchant/menu.html")

# # Order routes
# @app.route("/order/create", methods=["GET", "POST"])
# def create_order():
#     # Handle order creation logic
#     return render_template("order/create.html")

# @app.route("/order/detail/<order_id>")
# def order_detail(order_id):
#     # Display order detail
#     return render_template("order/detail.html", order_id=order_id)

# @app.route("/order/history")
# def order_history():
#     # Display order history
#     return render_template("order/history.html")

# if __name__ == "__main__":
#     app.run()


##############################################################################


import os
import subprocess


# 导入subprocess模块，用于调用系统命令来安装依赖项

def install_dependencies():
    # 获取当前文件(main.py)所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接requirements.txt文件的路径
    # requirements_path = os.path.join(current_dir, 'requirements.txt')
    # subprocess.check_call(['pip', 'install', '-r', requirements_path])
    current_dir = os.path.dirname(os.path.abspath(__file__))
    requirements_path = os.path.join(current_dir, '..', 'requirements.txt')
    subprocess.check_call(['pip', 'install', '-r', requirements_path])


if __name__ == '__main__':
    # 在主程序入口处调用安装依赖项的函数
    install_dependencies()

from flask import Flask, render_template

# 导入Flask类和render_template函数


app = Flask(__name__, template_folder="../templates")


# app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    # 定义根路由，返回渲染后的index.html模板页面    user/   /login


@app.route("/user/login", methods=["GET", "POST"])
def user_login():
    return render_template("user/login.html")
    # 定义用户登录页面的路由，支持GET和POST请求方法，返回渲染后的user/login.html模板页面


# @app.route("/login1", methods=["GET", "POST"])
# def user_login1():
#     return render_template("login1.html")
#     # 定义用户登录页面的路由，支持GET和POST请求方法，返回渲染后的user/login.html模板页面
#
# @app.route("/user/login1", methods=["GET", "POST"])
# def user_login2():
#     return render_template("user/login1.html")
#     # 定义用户登录页面的路由，支持GET和POST请求方法，返回渲染后的user/login.html模板页面


@app.route("/user/register", methods=["GET", "POST"])
def user_register():
    return render_template("user/register.html")
    # 定义用户注册页面的路由，支持GET和POST请求方法，返回渲染后的user/register.html模板页面


@app.route("/user/profile")
def user_profile():
    return render_template("user/profile.html")
    # 定义用户个人资料页面的路由，返回渲染后的user/profile.html模板页面


@app.route("/merchant/login", methods=["GET", "POST"])
def merchant_login():
    return render_template("merchant/login.html")
    # 定义商家登录页面的路由，支持GET和POST请求方法，返回渲染后的merchant/login.html模板页面


@app.route("/merchant/register", methods=["GET", "POST"])
def merchant_register():
    return render_template("merchant/register.html")
    # 定义商家注册页面的路由，支持GET和POST请求方法，返回渲染后的merchant/register.html模板页面


@app.route("/merchant/dashboard")
def merchant_dashboard():
    return render_template("merchant/dashboard.html")
    # 定义商家仪表盘页面的路由，返回渲染后的merchant/dashboard.html模板页面


@app.route("/merchant/menu")
def merchant_menu():
    return render_template("merchant/menu.html")
    # 定义商家菜单页面的路由，返回渲染后的merchant/menu.html模板页面


@app.route("/order/create", methods=["GET", "POST"])
def create_order():
    return render_template("order/create.html")
    # 定义创建订单页面的路由，支持GET和POST请求方法，返回渲染后的order/create.html模板页面


@app.route("/order/detail/<order_id>")
def order_detail(order_id):
    return render_template("order/detail.html", order_id=order_id)
    # 定义订单详情页面的路由，使用动态路由参数order_id接收订单ID作为参数，返回渲染后的order/detail.html模板页面

@app.route("/order/detail", methods=["GET", "POST"])
def order_detail1():
    return render_template("order/detail.html")


@app.route("/order/history")
def order_history():
    return render_template("order/history.html")
    # 定义订单历史记录页面的路由，返回渲染后的order/history.html模板页面


if __name__ == '__main__':
    app.run()
    # 如果当前模块是主程序入口，则运行Flask应用程序
