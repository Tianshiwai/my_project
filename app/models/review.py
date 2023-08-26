class Review:
    def __init__(self, user, merchant, rating, comment):
        self.user = user
        self.merchant = merchant
        self.rating = rating
        self.comment = comment

    def submit(self):
        # 提交评论逻辑
        pass

    def update(self, rating=None, comment=None):
        # 更新评论逻辑
        pass

    def delete(self):
        # 删除评论逻辑
        pass