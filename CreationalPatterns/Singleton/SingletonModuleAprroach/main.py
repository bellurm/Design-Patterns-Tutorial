from singleton_module import singleton_instance

# singleton_instance üzerinde işlem yapıyoruz
singleton_instance.value = 42
print(f"singleton_instance.value in main: {singleton_instance.value}")

# Başka bir modül veya fonksiyon içinde singleton_instance kullanımı
import another_module
another_module.print_singleton_value()