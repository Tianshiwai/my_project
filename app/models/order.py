class Order:
    def __init__(self, user, merchant, menu, quantity):
        self.user = user
        self.merchant = merchant
        self.menu = menu
        self.quantity = quantity

    def create(self):
        # 创建订单逻辑
        pass

    def update(self, **kwargs):
        # 更新订单信息逻辑
        pass

    def cancel(self):
        # 取消订单逻辑
        pass

    def calculate_total_price(self):
        # 计算订单总价逻辑
        pass