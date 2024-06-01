# ÖRNEK 1
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
        self._update_area()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update_area()

    @property
    def area(self):
        return self._width * self._height

    def _update_area(self):
        print(f"Updated area: {self.area}")

# Kullanım
rect = Rectangle(5, 10)
rect.width = 7  # Output: Updated area: 70
rect.height = 3  # Output: Updated area: 21

print("#"*70)

# ÖRNEK 2
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = width * height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._update_area()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update_area()

    @property
    def area(self):
        return self._area

    def _update_area(self):
        self._area = self._width * self._height
        print(f'Area updated: {self._area}')


# Kullanım
rectangle = Rectangle(5, 10)

print(f'Initial area: {rectangle.area}')  # Output: Initial area: 50

rectangle.width = 7
rectangle.height = 3

# Çıktı:
# Area updated: 70
# Area updated: 21
