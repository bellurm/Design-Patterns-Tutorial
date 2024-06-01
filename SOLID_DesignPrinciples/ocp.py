# Open-Closed Principle (Açık-Kapalı Prensibi - OCP), yazılım tasarımının beş temel prensibinden biridir ve SOLID prensipleri arasında yer alır.
# Bu prensip, yazılım bileşenlerinin (sınıflar, modüller, fonksiyonlar vb.) açık (open) olması, yani genişletilebilir olması, ancak değiştirilemez (closed) olması gerektiğini belirtir.

# Açık-Kapalı Prensibi, mevcut kodu değiştirmeden yeni işlevsellik eklemeyi mümkün kılar.
# Bunu sağlamak için mevcut kodu değiştirmek yerine, var olan kodu genişletmek için esneklik sağlayan bir tasarımı teşvik eder.

# Bu prensibi uygulamak için genellikle şu yöntemler kullanılır:
# Soyutlama (Abstraction): Kodda değişmeye eğilimli olan kısımları soyutlama yoluyla ayırmak, böylece bu kısımları değiştirmek yerine genişletmek mümkün olur.
# Polimorfizm: Polimorfizm, farklı nesnelerin aynı arabirimi uygulayabilmesini sağlar. Böylece, yeni bir işlevsellik eklemek için var olan sınıfları değiştirmeden yeni sınıflar oluşturulabilir.
# Kalıtım (Inheritance): Var olan bir sınıfın özelliklerini ve davranışlarını başka bir sınıfa miras alarak genişletmek.

# Open-Closed Principle, kodun daha esnek, yeniden kullanılabilir ve bakımı daha kolay hale gelmesini sağlar.
# Kodun bir kısmını değiştirmeden yeni işlevsellik eklemek, hatalı kodu en aza indirir ve kodun daha sağlam olmasını sağlar.
# Bu nedenle, yazılım geliştirme sürecinde OCP'ye uygun bir tasarım prensibi benimsemek önemlidir.

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size, weight):
        self.name = name
        self.color = color
        self.size = size
        self.weight = weight

class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class WeightSpecification(Specification):
    def __init__(self, weight):
        self.weight = weight
    
    def is_satisfied(self, item):
        return item.weight == self.weight

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL, 100)
tree = Product('Tree', Color.GREEN, Size.LARGE, 500)
house = Product('House', Color.BLUE, Size.LARGE, 10000)

products = [apple, tree, house]

bf = BetterFilter()

print('Green products:')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
large_and_blue = BetterFilter()
for p in bf.filter(products, large):
    if p.color == Color.BLUE:
        print(f' - {p.name} is large and blue')

print("Products with weight 100:")
weight_100 = WeightSpecification(100)
for p in bf.filter(products, weight_100):
     print(f' - {p.name} has weight 100')
     