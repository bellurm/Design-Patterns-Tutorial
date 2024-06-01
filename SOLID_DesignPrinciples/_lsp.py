# Liskov Substitution Principle (LSP), bir alt sınıfın, üst sınıfın yerini alabilmesi gerektiğini belirtir,
# yani alt sınıfın nesneleri, üst sınıfın nesneleri yerine kullanılabilmelidir ve programın doğru çalışması gerekmektedir.
# Bu, alt sınıfların, üst sınıfların beklenen davranışlarını değiştirmemesi gerektiği anlamına gelir.
# Örneğin, bir "Kare" sınıfı, "Dikdörtgen" sınıfının alt sınıfı olmamalıdır, çünkü "Kare" sınıfı,
# "Dikdörtgen" sınıfının tüm yöntemlerini düzgün bir şekilde devralamaz ve bu da programın mantığını bozabilir.

# ÖRNEK 1
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")


# ÖRNEK 2
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value


# ÖRNEK 3
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

class Order:
    def __init__(self, amount, payment_processor: PaymentProcessor):
        self.amount = amount
        self.payment_processor = payment_processor

    def complete_order(self):
        self.payment_processor.process_payment(self.amount)
