from models.customer import Customer
import datetime

class CustomerService:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo

    def create_customer(self,data):

        existing_customer = self.customer_repo.find_by_email(data.get('email'))
        if existing_customer:
            return {'error': 'Email already exists'}, 400

        new_customer = Customer(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            phone = data.get('phone'),
            company = data.get('company')
        )
        self.customer_repo.create(new_customer)
        return {"message": "Customer created successfully", "customer_id": new_customer.customer_id}, 201

    def get_customer(self,customer_id):
        customer = self.customer_repo.get_by_id(customer_id)

        if not customer:
            return {'error', 'Customer not found'}, 404
        customer.pop('_id',None)
        return customer, 200

    def delete_customer(self,customer_id):
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            return {"error": "Customer not found"}, 404

        deletion_time = datetime.datetime.now()
        self.customer_repo.soft_delete(customer_id,deletion_time)
        return {"message": "deletion succeed"}, 200

    def update_customer(self,customer_id, data):
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            return {"error": "Customer not found"}, 404
        update_fields = {
            "first_name": data.get("first_name", customer.get("first_name")),
            "last_name": data.get("last_name", customer.get("last_name")),
            "phone": data.get("phone", customer.get("phone")),
            "company": data.get("company", customer.get("company")),
            "updated_at": datetime.datetime.now()  # עדכון זמן השינוי
        }
        self.customer_repo.update(customer_id, update_fields)
        return {"message": "Update succeed"} , 200


