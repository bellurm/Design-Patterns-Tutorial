import threading

class CustomerAllocator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.customer_data = {}
        return cls._instance

    def get_customer_data(self):
        return self.customer_data

    def update_customer_data(self, customer_id, data):
        with self._lock:
            if customer_id in self.customer_data:
                self.customer_data[customer_id].update(data)
            else:
                self.customer_data[customer_id] = data

class CRMSystem:
    def __init__(self, customer_allocator):
        self.customer_allocator = customer_allocator

    def view_customer_data(self, customer_id):
        customer_data = self.customer_allocator.get_customer_data()
        if customer_id in customer_data:
            print(f"Customer Data for Customer ID {customer_id}: {customer_data[customer_id]}")
        else:
            print(f"Customer ID {customer_id} not found.")

    def update_customer_data(self, customer_id, data):
        self.customer_allocator.update_customer_data(customer_id, data)
        print(f"Customer Data for Customer ID {customer_id} updated successfully.")

# Singleton olarak CustomerAllocator örneği oluşturuluyor
customer_allocator = CustomerAllocator()

# CRMSystem örneği oluşturuluyor ve CustomerAllocator örneği parametre olarak iletiliyor
crm_system = CRMSystem(customer_allocator)

# Müşteri verileri görüntüleniyor
crm_system.view_customer_data(1)

# Müşteri verileri güncelleniyor
crm_system.update_customer_data(1, {"name": "John", "email": "john@example.com"})

# Güncellenmiş müşteri verileri görüntüleniyor
crm_system.view_customer_data(1)
