class SupermarketCheckout:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.total_sales = 0.0
            cls._instance.transactions = []
        return cls._instance

    def scan_item(self, item_price):
        self.total_sales += item_price
        self.transactions.append(item_price)
        print(f"Scanned item with price: {item_price}. Total sales: {self.total_sales}")

    def get_total_sales(self):
        return self.total_sales

    def get_transactions(self):
        return self.transactions

def main():
    checkout1 = SupermarketCheckout()
    checkout2 = SupermarketCheckout()

    # Ürün tarama ve toplam satışları görüntüleme
    checkout1.scan_item(10.0)
    checkout1.scan_item(5.5)

    print(f"Checkout1 Total Sales: {checkout1.get_total_sales()}")

    # İkinci kasadan ürün tarama ve toplam satışları görüntüleme
    checkout2.scan_item(20.0)
    print(f"Checkout2 Total Sales: {checkout2.get_total_sales()}")

    # Her iki kasa da aynı nesneye işaret ettiği için toplam satışlar ve işlemler her ikisi için de aynıdır
    print(f"Checkout1 Transactions: {checkout1.get_transactions()}")
    print(f"Checkout2 Transactions: {checkout2.get_transactions()}")

    # Aynı nesneye işaret ettiklerini doğrulama
    print(f"checkout1 is checkout2: {checkout1 is checkout2}")

if __name__ == "__main__":
    main()
