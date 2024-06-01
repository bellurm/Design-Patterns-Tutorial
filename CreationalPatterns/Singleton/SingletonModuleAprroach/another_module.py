from singleton_module import singleton_instance

def print_singleton_value():
    print(f"singleton_instance.value in another_module: {singleton_instance.value}")

# Fonksiyonu çağırarak değer kontrolü yapıyoruz
print_singleton_value()
