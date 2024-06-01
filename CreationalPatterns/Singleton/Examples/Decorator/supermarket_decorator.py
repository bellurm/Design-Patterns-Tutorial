def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class SupermarketCheckout:
    def __init__(self):
        self.total_sales = 0.0
        self.transactions = []

    def scan_item(self, item_price):
        self.total_sales += item_price
        self.transactions.append(item_price)
        print(f"Scanned item with price: {item_price}. Total sales: {self.total_sales}")

    def get_total_sales(self):
        return self.total_sales

    def get_transactions(self):
        return self.transactions

# Kullanım
if __name__ == "__main__":
    checkout1 = SupermarketCheckout()
    checkout2 = SupermarketCheckout()

    # Ürün tarama ve toplam satışları görüntüleme
    checkout1.scan_item(10.0)
    checkout1.scan_item(5.5)

    print(f"Checkout1 Total Sales: {checkout1.get_total_sales()}")  # Çıktı: Checkout1 Total Sales: 15.5

    # İkinci kasadan ürün tarama ve toplam satışları görüntüleme
    checkout2.scan_item(20.0)
    print(f"Checkout2 Total Sales: {checkout2.get_total_sales()}")  # Çıktı: Checkout2 Total Sales: 35.5

    # Her iki kasa da aynı nesneye işaret ettiği için toplam satışlar ve işlemler her ikisi için de aynıdır
    print(f"Checkout1 Transactions: {checkout1.get_transactions()}")  # Çıktı: Checkout1 Transactions: [10.0, 5.5, 20.0]
    print(f"Checkout2 Transactions: {checkout2.get_transactions()}")  # Çıktı: Checkout2 Transactions: [10.0, 5.5, 20.0]

    # Aynı nesneye işaret ettiklerini doğrulama
    print(f"checkout1 is checkout2: {checkout1 is checkout2}")  # Çıktı: True
