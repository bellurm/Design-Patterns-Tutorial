from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_amount):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total_amount):
        return total_amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        return total_amount * (1 - self.percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total_amount):
        return total_amount - self.discount_amount

class CheckoutService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_total(self, cart):
        total_amount = sum(item.price for item in cart)
        return self.discount_strategy.apply_discount(total_amount)

# Burada OCP yaklaşımıyla bir indirim yapıyoruz. DiscountStrategy arayüzü kullanılarak farklı indirim stratejileri yazılabilir.
# CheckoutService class'ı işlemleri yapan class olduğundan, yeni bir indirim class'ı oluştururken herhangi bir class etkilenmez ve
# CheckoutService bu işi kolaylıkla kabul edip yapar. Bu durum Open-Closed yaklaşımını güzel betimler.
