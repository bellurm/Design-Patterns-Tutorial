from abc import ABC, abstractmethod
from PIL import Image as PILImage
import time

# Subject
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")
        self.image = PILImage.open(self.filename)
        time.sleep(2)  # Simulating a delay in loading the image

    def display(self):
        if self.image:
            self.image.show()
        else:
            print("Image not loaded")

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
    image = ProxyImage(r"path\to\your\image.jpg")
    # First display: Image will be loaded and displayed
    image.display()
    # Second display: Image will not be loaded again, only displayed
    image.display()

if __name__ == "__main__":
    main()
