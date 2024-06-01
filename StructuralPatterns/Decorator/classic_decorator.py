# ÖRNEK 1
class TextComponent:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

class BoldDecorator(TextComponent):
    def __init__(self, component):
        self._component = component

    def render(self):
        return f"<b>{self._component.render()}</b>"

class ItalicDecorator(TextComponent):
    def __init__(self, component):
        self._component = component

    def render(self):
        return f"<i>{self._component.render()}</i>"

# Kullanım
text = TextComponent("Hello, World!")
bold_text = BoldDecorator(text)
italic_bold_text = ItalicDecorator(bold_text)

print(italic_bold_text.render())

print("#"*70)

# ÖRNEK 2

from abc import ABC, abstractmethod

# Component
class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

# Concrete Component
class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def read_data(self):
        with open(self._filename, 'r') as file:
            return file.read()

# Decorator
class DataSourceDecorator(DataSource):
    def __init__(self, wrappee):
        self._wrappee = wrappee

    def read_data(self):
        return self._wrappee.read_data()

# Concrete Decorators
class EncryptionDecorator(DataSourceDecorator):
    def read_data(self):
        data = super().read_data()
        return self._encrypt(data)

    def _encrypt(self, data):
        return ''.join(chr(ord(char) + 1) for char in data)  # Basit şifreleme (Caesar cipher)

class CompressionDecorator(DataSourceDecorator):
    def read_data(self):
        data = super().read_data()
        return self._compress(data)

    def _compress(self, data):
        return ''.join(char for i, char in enumerate(data) if i % 2 == 0)  # Basit sıkıştırma


if __name__ == "__main__":
    # Dosya okuma için temel veri kaynağı
    file_data_source = FileDataSource('data.txt')

    # Şifreleme ve sıkıştırma dekoratörleri ile veri kaynağını süsleme
    encrypted_data_source = EncryptionDecorator(file_data_source)
    compressed_encrypted_data_source = CompressionDecorator(encrypted_data_source)

    # Veriyi oku ve işle
    print(compressed_encrypted_data_source.read_data())
