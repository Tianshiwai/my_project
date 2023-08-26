from models.menu import Menu

def create():
    if request.method == 'POST':
        # 处理创建菜单请求
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        menu = Menu(name, price, description)
        menu.create()
        # 其他处理逻辑

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