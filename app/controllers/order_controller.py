from models.order import Order

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

def update():
    if request.method == 'POST':
        # 处理更新订单请求
        order_id = request.form['order_id']
        new_quantity = request.form['new_quantity']
        order = Order(order_id, '', '', new_quantity)
        order.update()
        # 其他处理逻辑
