import Singleton.Examples.Module.supermarket_module as supermarket_module

def main():
    checkout_instance = supermarket_module.SupermarketCheckout()

    checkout1 = supermarket_module.SupermarketCheckout.get_instance()
    checkout2 = supermarket_module.SupermarketCheckout.get_instance()

    # Ürün tarama ve toplam satışları görüntüleme
    supermarket_module.SupermarketCheckout.scan_item(10.0)
    supermarket_module.SupermarketCheckout.scan_item(5.5)

    print(f"Checkout1 Total Sales: {supermarket_module.SupermarketCheckout.get_total_sales()}")  # Çıktı: Checkout1 Total Sales: 15.5

    # İkinci kasadan ürün tarama ve toplam satışları görüntüleme
    supermarket_module.SupermarketCheckout.scan_item(20.0)
    print(f"Checkout2 Total Sales: {supermarket_module.SupermarketCheckout.get_total_sales()}")  # Çıktı: Checkout2 Total Sales: 35.5

    # Her iki kasa da aynı nesneye işaret ettiği için toplam satışlar ve işlemler her ikisi için de aynıdır
    print(f"Checkout1 Transactions: {supermarket_module.SupermarketCheckout.get_transactions()}")  # Çıktı: Checkout1 Transactions: [10.0, 5.5, 20.0]
    print(f"Checkout2 Transactions: {supermarket_module.SupermarketCheckout.get_transactions()}")  # Çıktı: Checkout2 Transactions: [10.0, 5.5, 20.0]

    # Aynı nesneye işaret ettiklerini doğrulama
    print(f"checkout1 is checkout2: {checkout1 is checkout2}")  # Çıktı: True

if __name__ == "__main__":
    main()
