from flask import Blueprint, jsonify, request

customer_bp = Blueprint('customer_bp', __name__)

def init_customer_routes(customer_service):
    @customer_bp.route('/')
    def home():
        return {"message": "Customer service is up!"}

    @customer_bp.route('/customer', methods=['POST'])
    def create_customer():
        data = request.get_json()
        result, status_code = customer_service.create_customer(data)
        return jsonify(result), status_code

    @customer_bp.route('/customer/<customer_id>', methods=['GET'])
    def get_customer(customer_id):
        result, status_code = customer_service.get_customer(customer_id)
        return jsonify(result), status_code

    @customer_bp.route('/customer/<customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        result, status_code = customer_service.delete_customer(customer_id)
        return jsonify(result), status_code

    @customer_bp.route('/customer/<customer_id>', methods=['PUT'])
    def update(customer_id):
        data = request.get_json()
        result, status_code = customer_service.update_customer(customer_id, data)
        return jsonify(result), status_code

    return customer_bp