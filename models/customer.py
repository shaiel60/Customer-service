from enum import Enum
import uuid
from datetime import datetime

class CustomerStatus(Enum):
    LEAD = "lead"
    ACTIVE = "active"
    INACTIVE = "inactive"

class Customer:
    def __init__(self, first_name, last_name, email, phone, company = None, status = None, updated_at = None):
        self.customer_id = str(uuid.uuid4()) # unique identifier for customer using UUID
        self.created_at = datetime.now() # creation date of customer
        self.deleted_at = None # Deletion flag - if None-> customer exist , else -> it deleted
        self.status = status or CustomerStatus.LEAD.value # status
        self.updated_at = updated_at

        #properties
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.company = company
