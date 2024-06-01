### Bu yaklaşımda, sınıfın yalnızca bir kez örneklendiğinden emin olmak için sınıfın __new__ ve __init__ metodlarını kontrol ederiz. ###

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.value = None

# Kullanım
singleton1 = Singleton()
singleton2 = Singleton()

singleton1.value = 42
print(f"singleton1.value: {singleton1.value}")  # Çıktı: singleton1.value: 42

singleton2.value = 100
print(f"singleton1.value: {singleton1.value}")  # Çıktı: singleton1.value: 100
print(f"singleton2.value: {singleton2.value}")  # Çıktı: singleton2.value: 100

print(f"singleton1 is singleton2: {singleton1 is singleton2}")  # Çıktı: True
