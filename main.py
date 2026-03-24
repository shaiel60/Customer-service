from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService
from routes.routes import customer_bp, init_customer_routes
import os

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

customer_repo = CustomerRepository(mongo.db) # creation of repository and connection to the DB
customer_service = CustomerService(customer_repo) # creation of service and injection of repo to it

init_customer_routes(customer_service)
app.register_blueprint(customer_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
