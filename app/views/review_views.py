from flask import Blueprint, render_template, request
from models.review import Review

review_blueprint = Blueprint('review', __name__)

@review_blueprint.route('/submit', methods=['GET', 'POST'])
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
    return render_template('review/submit.html')

@review_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # 处理更新评论请求
        review_id = request.form['review_id']
        new_rating = request.form['new_rating']
        new_comment = request.form['new_comment']
        review = Review(review_id, '', new_rating, new_comment)
        review.update()
        # 其他处理逻辑
    return render_template('review/update.html')