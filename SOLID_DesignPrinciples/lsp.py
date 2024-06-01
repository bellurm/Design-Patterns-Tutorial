# Liskov Substitution Principle (LSP), yazılım tasarımında bir alt sınıfın, üst sınıfın yerine geçebilir olması gerektiğini belirten bir prensiptir.

# LSP, bir türetilmiş sınıfın, temel sınıfın tüm davranışlarını aynı şekilde sergileyebilmesi gerektiğini ifade eder.
# Yani, bir alt sınıfın, temel sınıfın tüm davranışlarını değiştirmeden kullanılabilmesi gerekmektedir.

# Bu prensibin temelinde, türetilmiş sınıfların üst sınıflarının yerine kullanılabilir olması ve kodun beklenen şekilde davranış göstermesi yatar.
# Bu da yazılımın esnekliğini ve değişime uyum kabiliyetini artırır.

# Liskov Substitution Principle'ın anahtar noktaları şunlardır:
# Bir alt sınıfın, üst sınıfın tüm davranışlarını (metodları) sağlaması gerekir.
# Alt sınıflar, üst sınıfların davranışlarını bozmamalı veya değiştirmemelidir.
# Alt sınıflar, üst sınıfın belirtilen davranışlarını daha spesifik hale getirebilir veya yeni davranışlar ekleyebilir, ancak mevcut davranışları değiştirmemelidir.

# Bu prensip, kodun doğru ve tutarlı bir şekilde çalışmasını sağlar ve yazılımın bakımını ve genişletilebilirliğini artırır.
# Ayrıca, polimorfizm gibi kavramları etkin bir şekilde kullanmanın önemini vurgular.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

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

class Square(Shape):
    def __init__(self, size):
        self._size = size

    def area(self):
        return self._size ** 2

    def __str__(self):
        return f'Size: {self._size}'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

def use_it(shape):
    expected = shape.area()
    print(f'Expected an area of {expected}, got {shape.area()}')

rectangle = Rectangle(2, 3)
use_it(rectangle)

square = Square(5)
use_it(square)
