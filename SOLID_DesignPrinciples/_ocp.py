# Open-Closed Principle (OCP), bir yazılım varlığının (sınıf, modül, fonksiyon) yeni davranışlar eklemek için açık,
# ancak mevcut davranışları değiştirmek için kapalı olması gerektiğini ifade eder.
# Yani, mevcut kodu değiştirmeden yeni özellikler ekleyebilmelisiniz.
# Bunu sağlamak için, yeni davranışları mevcut sınıfların miras alınması veya kompozisyon kullanarak genişletmek suretiyle ekleyebilirsiniz.
# Örneğin, bir ödeme sistemi sınıfını düşünün; bu sınıfa yeni bir ödeme yöntemi eklemek için mevcut sınıfı değiştirmek yerine yeni bir alt sınıf oluşturabilirsiniz.

# ÖRNEK 1
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# ÖRNEK 2
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount * (1 - self.percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return amount - self.discount_amount

class Order:
    def __init__(self, amount, discount_strategy: DiscountStrategy):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def get_total(self):
        return self.discount_strategy.apply_discount(self.amount)


# ÖRNEK 3
from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class PDFReportGenerator(ReportGenerator):
    def generate(self, data):
        # Generate PDF report
        print(f"Generating PDF report with data: {data}")

class HTMLReportGenerator(ReportGenerator):
    def generate(self, data):
        # Generate HTML report
        print(f"Generating HTML report with data: {data}")

class ReportService:
    def __init__(self, report_generator: ReportGenerator):
        self.report_generator = report_generator

    def create_report(self, data):
        self.report_generator.generate(data)
