# Virtual Proxy ile büyük bir resim dosyasını yüklemek
from abc import ABC, abstractmethod

# Subject
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client
def main():
    image = ProxyImage("test_image.jpg")
    # Image will be loaded and displayed
    image.display()
    # Image will not be loaded again, only displayed
    image.display()

if __name__ == "__main__":
    main()
