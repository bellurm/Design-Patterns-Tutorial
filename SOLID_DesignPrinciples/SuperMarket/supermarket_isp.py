from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class OnlinePaymentMethod(PaymentMethod):
    @abstractmethod
    def validate_online(self):
        pass

class OfflinePaymentMethod(PaymentMethod):
    @abstractmethod
    def validate_offline(self):
        pass

class CreditCardPayment(OnlinePaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

    def validate_online(self):
        print("Validating credit card online.")

class CashPayment(OfflinePaymentMethod):
    def process_payment(self, amount):
        print(f"Processing cash payment of {amount}")

    def validate_offline(self):
        print("Validating cash payment offline.")

# PaymentMethod olarak tanımlanan sınıf ortak özellikleri tutarken ISP'ye uygun bir hale getirmek için yaratılan
# OnlinePaymentMethod ve OfflinePaymentMethod sınıflarındaki metotlar @abstractmethod olarak uygulanır.
# Sonrasında CreditCardPayment ve CashPayment sınıfları OnlinePaymentMethod ve OfflinePaymentMethod sınıflarıyla
# paralel çalışacaktır. Bu sayede bir class içerisinde kullanılmayan bir metot oluşturulmamış olacaktır.
# Örneğin CreditCardPayment ve CashPayment sınıfları sadece bir sınıftan veri çekiyor olsalardı, gelen müşteri de
# nakit para ile ödeme yapacak olsaydı CreditCardPayment sınıfı çalışmayacaktı. Bu da istenmeyen bir durumdur.
