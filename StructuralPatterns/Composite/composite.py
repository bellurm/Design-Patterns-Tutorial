# ÖRNEK 1
from abc import ABC, abstractmethod

# Component: Ortak arayüz
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf: Yaprak nesne
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"File: {self.name}")

# Composite: Bileşik nesne
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def show_details(self):
        print(f"Directory: {self.name}")
        for component in self.components:
            component.show_details()

# Client kodu
if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    dir1 = Directory("dir1")
    dir2 = Directory("dir2")

    dir1.add_component(file1)
    dir1.add_component(file2)

    dir2.add_component(file3)
    dir2.add_component(dir1)

    dir2.show_details()
    
    print("*"*50)
    
    dir1.remove_component(file1)
    dir1.show_details()
    
print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# Component: Ortak arayüz
class Employee(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Leaf: Bireysel Çalışan
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"{self.position}: {self.name}"

class Designer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"{self.position}: {self.name}"

# Composite: Yönetici
class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add(self, employee):
        self.subordinates.append(employee)

    def remove(self, employee):
        self.subordinates.remove(employee)

    def get_details(self):
        details = f"{self.position}: {self.name}\n"
        for subordinate in self.subordinates:
            details += "  " + subordinate.get_details() + "\n"
        return details.strip()

# Client kodu
if __name__ == "__main__":
    dev1 = Developer("Alice", "Senior Developer")
    dev2 = Developer("Bob", "Junior Developer")
    designer1 = Designer("Charlie", "Senior Designer")

    manager1 = Manager("David", "Development Manager")
    manager1.add(dev1)
    manager1.add(dev2)

    general_manager = Manager("Eve", "General Manager")
    general_manager.add(manager1)
    general_manager.add(designer1)

    print(general_manager.get_details())
