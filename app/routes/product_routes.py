from flask import Blueprint, request, jsonify
from app.controllers.product_controller import *

product_bp = Blueprint('products', __name__, url_prefix='/products')

@product_bp.route('/add', methods=['POST'])
def add_product_route():
    product_data = request.get_json()
    response = add_product(product_data)
    return jsonify(response)

@product_bp.route('/<product_id>', methods=['GET'])
def get_product_route(product_id):
    response = get_product(product_id)
    return jsonify(response)

@product_bp.route('/', methods=['GET'])
def get_all_products_route():
    response = get_all_products()
    return jsonify({'data' : response})

@product_bp.route('/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    response = update_product(product_id, data)
    return jsonify(response)

@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    response = delete_product(product_id)
    return jsonify(response)
