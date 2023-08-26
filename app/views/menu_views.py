from flask import Blueprint, render_template, request
from models.menu import Menu

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # 处理创建菜单请求
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        menu = Menu(name, price, description)
        menu.create()
        # 其他处理逻辑
    return render_template('menu/create.html')

@menu_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # 处理更新菜单请求
        menu_id = request.form['menu_id']
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        menu = Menu(name, price, description)
        menu.update()
        # 其他处理逻辑
    return render_template('menu/update.html')