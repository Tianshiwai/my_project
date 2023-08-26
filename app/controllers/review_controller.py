from models.review import Review

def submit():
    if request.method == 'POST':
        # 处理提交评论请求
        user_id = request.form['user_id']
        merchant_id = request.form['merchant_id']
        rating = request.form['rating']
        comment = request.form['comment']
        review = Review(user_id, merchant_id, rating, comment)
        review.submit()
        # 其他处理逻辑

def update():
    if request.method == 'POST':
        # 处理更新评论请求
        review_id = request.form['review_id']
        new_rating = request.form['new_rating']
        new_comment = request.form['new_comment']
        review = Review(review_id, '', new_rating, new_comment)
        review.update()
        # 其他处理逻辑