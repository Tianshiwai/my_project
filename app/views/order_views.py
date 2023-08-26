from flask import Blueprint, render_template, request
from models.order import Order

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # 处理创建订单请求
        user_id = request.form['user_id']
        merchant_id = request.form['merchant_id']
        menu_id = request.form['menu_id']
        quantity = request.form['quantity']
        order = Order(user_id, merchant_id, menu_id, quantity)
        order.create()
        # 其他处理逻辑
    return render_template('order/create.html')

@order_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # 处理更新订单请求
        order_id = request.form['order_id']
        new_quantity = request.form['new_quantity']
        order = Order(order_id, '', '', new_quantity)
        order.update()
        # 其他处理逻辑
    return render_template('order/update.html')