from flask import Blueprint, render_template, request
from models.delivery import Delivery

delivery_blueprint = Blueprint('delivery', __name__)

@delivery_blueprint.route('/update_status', methods=['POST'])
def update_status():
    # 处理更新配送状态请求
    delivery_id = request.form['delivery_id']
    new_status = request.form['new_status']
    delivery = Delivery(delivery_id, '', new_status)
    delivery.update_status()
    # 其他处理逻辑
    return ''

@delivery_blueprint.route('/get_estimated_delivery_time', methods=['GET'])
def get_estimated_delivery_time():
    # 处理获取预计配送时间请求
    delivery_id = request.args.get('delivery_id')
    delivery = Delivery(delivery_id, '', '')
    estimated_delivery_time = delivery.get_estimated_delivery_time()
    # 其他处理逻辑
    return str(estimated_delivery_time)