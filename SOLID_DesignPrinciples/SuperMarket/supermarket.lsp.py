from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class CashPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing cash payment of {amount}")

class Order:
    def __init__(self, amount, payment_processor: PaymentProcessor):
        self.amount = amount
        self.payment_processor = payment_processor

    def complete_order(self):
        self.payment_processor.process_payment(self.amount)

# Bu örnekte yapılan şey, çeşitli yöntemlerle ödeme almaktır. Ödeme alma işleminin ortak özelliklerini (amount: tutar)
# tutan PaymentProcessor class'ı, içerisindeki metodu @abstractmethod olarak kullanır. Bunun sebebi, bu metodun diğer
# sınıflarda da rahatça ve mecbur ederek kullanılabilmesini sağlamaktır.
# CreditCardPaymentProcessor, PayPalPaymentProcessor ve CashPaymentProcessor sınıfları ödeme yöntemlerini belirlerken
# Order sınıfı, üst sınıfların işleyişini ve özelliklerini değiştirmeden hepsinden bilgi çekip tüm işleri halledecektir.
# Bu da güzel bir LSP örneğidir.
