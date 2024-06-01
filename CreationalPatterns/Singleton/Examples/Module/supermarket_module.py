class SupermarketCheckout:
    _instance = None

    def __init__(self):
        if not SupermarketCheckout._instance:
            SupermarketCheckout._instance = self
            self.total_sales = 0.0
            self.transactions = []

    @staticmethod
    def get_instance():
        return SupermarketCheckout._instance

    @staticmethod
    def scan_item(item_price):
        instance = SupermarketCheckout.get_instance()
        instance.total_sales += item_price
        instance.transactions.append(item_price)
        print(f"Scanned item with price: {item_price}. Total sales: {instance.total_sales}")

    @staticmethod
    def get_total_sales():
        instance = SupermarketCheckout.get_instance()
        return instance.total_sales

    @staticmethod
    def get_transactions():
        instance = SupermarketCheckout.get_instance()
        return instance.transactions
