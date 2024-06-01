# ÖRNEK 1
from abc import ABC, abstractmethod

# Strategy Arayüzü
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

# Concrete Strategy Sınıfları
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage
    
    def apply_discount(self, price: float) -> float:
        return price - (price * self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount
    
    def apply_discount(self, price: float) -> float:
        return price - self.amount

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

# Context Sınıfı
class Product:
    def __init__(self, name: str, price: float, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy
    
    def get_price(self) -> float:
        return self.discount_strategy.apply_discount(self.price)

# Kullanım
product_a = Product("Product A", 100.0, PercentageDiscount(10))
product_b = Product("Product B", 100.0, FixedAmountDiscount(15))
product_c = Product("Product C", 100.0, NoDiscount())

print(f"{product_a.name} discounted price: {product_a.get_price()}")  # Output: 90.0
print(f"{product_b.name} discounted price: {product_b.get_price()}")  # Output: 85.0
print(f"{product_c.name} discounted price: {product_c.get_price()}")  # Output: 100.0

print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# Strategy Arayüzü
class TextFormatterStrategy(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass

# Concrete Strategy Sınıfları
class UpperCaseFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return text.upper()

class LowerCaseFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return text.lower()

class TitleCaseFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return text.title()

class ReverseTextFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return text[::-1]

# Context Sınıfı
class TextEditor:
    def __init__(self, formatter: TextFormatterStrategy):
        self.formatter = formatter
    
    def set_formatter(self, formatter: TextFormatterStrategy):
        self.formatter = formatter
    
    def publish_text(self, text: str) -> str:
        return self.formatter.format(text)

# Kullanım
editor = TextEditor(UpperCaseFormatter())
print(editor.publish_text("Hello World!"))  # Output: HELLO WORLD!

editor.set_formatter(LowerCaseFormatter())
print(editor.publish_text("Hello World!"))  # Output: hello world!

editor.set_formatter(TitleCaseFormatter())
print(editor.publish_text("hello world!"))  # Output: Hello World!

editor.set_formatter(ReverseTextFormatter())
print(editor.publish_text("Hello World!"))  # Output: !dlroW olleH
