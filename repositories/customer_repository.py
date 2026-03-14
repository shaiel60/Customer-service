from models.customer import Customer, CustomerStatus

class CustomerRepository:
    def __init__(self, db):
        self.collection = db.customers

    def create(self, customer_obj):
        customer_dict = {
            "customer_id": customer_obj.customer_id,
            "first_name": customer_obj.first_name,
            "last_name": customer_obj.last_name,
            "email": customer_obj.email,
            "phone": customer_obj.phone,
            "company": customer_obj.company,
            "status": customer_obj.status,
            "created_at": customer_obj.created_at,
            "deleted_at": customer_obj.deleted_at
        }
        return  self.collection.insert_one(customer_dict)

    def get_by_id(self, customer_id):
        # searching customer obj by its id
        return self.collection.find_one({
            "customer_id": customer_id,
            "deleted_at": None # if None is TRUE -> customer wasn't deleted
        })
    def find_by_email(self,email):
        return self.collection.find_one({
            "email": email,
            "deleted at": None
        })
    def soft_delete(self, customer_id, deletion_time):
        return self.collection.update_one({
            "customer_id": customer_id},
            {"$set": {"deleted_at": deletion_time}
        })

    def update(self,customer_id,update_data):
        return self.collection.update_one({
            "customer_id": customer_id},
            {"$set": update_data
        })