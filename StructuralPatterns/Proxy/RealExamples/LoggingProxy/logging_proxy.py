from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def create_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass

class RealFileSystem(FileSystem):
    def create_file(self, filename):
        print(f"Creating file: {filename}")

    def delete_file(self, filename):
        print(f"Deleting file: {filename}")

class LoggingProxy(FileSystem):
    def __init__(self, real_file_system):
        self.real_file_system = real_file_system
        self.log_file = open("file_system_log.txt", "a")

    def create_file(self, filename):
        self.log_file.write(f"Creating file: {filename}\n")
        self.real_file_system.create_file(filename)

    def delete_file(self, filename):
        self.log_file.write(f"Deleting file: {filename}\n")
        self.real_file_system.delete_file(filename)

    def __del__(self):
        self.log_file.close()

# Örnek Kullanım
def main():
    # Gerçek dosya sistemi ve kayıt proxy'si oluştur
    real_file_system = RealFileSystem()
    proxy = LoggingProxy(real_file_system)

    # Dosya oluşturma ve silme işlemlerini gerçekleştir
    proxy.create_file("example.txt")
    proxy.delete_file("example.txt")

if __name__ == "__main__":
    main()
