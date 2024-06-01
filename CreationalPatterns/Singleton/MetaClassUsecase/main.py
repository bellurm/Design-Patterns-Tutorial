# Metaclass, Python'da sınıfların nasıl oluşturulduğunu kontrol eden özel bir sınıf türüdür.
# Kısaca, sınıfları tanımlayan sınıflardır. Python'da her şey nesne olduğu için sınıflar da nesnelerdir ve
# bunlar metaclass'lar tarafından oluşturulur. Metaclass'lar, sınıfların nasıl davranacağını ve nasıl oluşturulacağını belirlemek için kullanılır.

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Kullanım
singleton1 = Singleton()
singleton2 = Singleton()

# Değer atama ve okuma
singleton1.value = 42
print(f"singleton1.value: {singleton1.value}")  # Çıktı: singleton1.value: 42

# İkinci referans üzerinden değeri değiştirme
singleton2.value = 100
print(f"singleton1.value: {singleton1.value}")  # Çıktı: singleton1.value: 100
print(f"singleton2.value: {singleton2.value}")  # Çıktı: singleton2.value: 100

# İki referansın aynı nesneye işaret ettiğini doğrulama
print(f"singleton1 is singleton2: {singleton1 is singleton2}")  # Çıktı: True
