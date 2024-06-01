# ÖRNEK 1
# Adapte Edilen Eski Sınıf
class OldPaymentSystem:
    def make_payment(self):
        return "Payment made using old system"

# Hedef (Yeni) Arayüz
class NewPaymentInterface:
    def pay(self):
        pass

# Adaptör Sınıfı
class PaymentAdapter(NewPaymentInterface):
    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self):
        return self.old_payment_system.make_payment()

# İstemci Kodu
def process_payment(payment_interface: NewPaymentInterface):
    print(payment_interface.pay())

# Kullanım
old_system = OldPaymentSystem()
adapter = PaymentAdapter(old_system)

process_payment(adapter)

print("#"*60)

# ÖRNEK 2
class OldCreditCardPayment:
    def pay_by_credit_card(self, amount: float):
        return f"Paid {amount} using old credit card system"
    
class PaymentProcessor:
    def process_payment(self, amount: float, payment_method: str):
        pass

class PaymentAdapter(PaymentProcessor):
    def __init__(self, old_credit_card_payment: OldCreditCardPayment):
        self.old_credit_card_payment = old_credit_card_payment

    def process_payment(self, amount: float, payment_method: str):
        if payment_method == "credit_card":
            return self.old_credit_card_payment.pay_by_credit_card(amount)
        elif payment_method == "paypal":
            return f"Paid {amount} using PayPal"
        else:
            return "Invalid payment method"

class PaymentClient:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def make_payment(self, amount: float, payment_method: str):
        return self.payment_processor.process_payment(amount, payment_method)

# Kullanım
old_credit_card_payment = OldCreditCardPayment()
payment_adapter = PaymentAdapter(old_credit_card_payment)
payment_client = PaymentClient(payment_adapter)

# Kredi kartı ile ödeme yapma
print(payment_client.make_payment(100.0, "credit_card"))

# PayPal ile ödeme yapma
print(payment_client.make_payment(200.0, "paypal"))

# Geçersiz ödeme yöntemi
print(payment_client.make_payment(150.0, "bitcoin"))
