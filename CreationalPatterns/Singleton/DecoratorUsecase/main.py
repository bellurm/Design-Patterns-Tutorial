def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton:
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
