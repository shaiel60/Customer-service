from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService
import os

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

customer_repo = CustomerRepository(mongo.db) # creation of repository and connection to the DB
customer_service = CustomerService(customer_repo) # creation of service and injection of repo to it

@app.route('/')
def home():
    return {"message": "Customer service is up!"}

@app.route('/customer', methods = ['POST'])
def create_customer():
    data = request.get_json()
    result, status_code = customer_service.create_customer(data)
    return jsonify(result), status_code

@app.route('/customer/<customer_id>', methods = ['GET'])
def get_customer(customer_id):
    result, status_code = customer_service.get_customer(customer_id)
    return jsonify(result), status_code

@app.route('/customer/<customer_id>', methods = ['DELETE'])
def delete_customer(customer_id):
    result , status_code = customer_service.delete_customer(customer_id)
    return jsonify(result), status_code

@app.route('/customer/<customer_id>', methods = ['PUT'])
def update(customer_id):
    data = request.get_json()
    result , status_code = customer_service.update_customer(customer_id, data)
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)
