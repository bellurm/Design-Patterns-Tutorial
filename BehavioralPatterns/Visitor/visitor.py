# ÖRNEK 1
from abc import ABC, abstractmethod

# Visitor Arayüzü
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass
    
    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# Concrete Visitor Sınıfları
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        area = 3.14 * (circle.radius ** 2)
        print(f"Circle area: {area}")
    
    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Rectangle area: {area}")

class DrawingTool(ShapeVisitor):
    def visit_circle(self, circle):
        print(f"Drawing a circle with radius {circle.radius}")
    
    def visit_rectangle(self, rectangle):
        print(f"Drawing a rectangle with width {rectangle.width} and height {rectangle.height}")

# Element Arayüzü
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass

# Concrete Element Sınıfları
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_rectangle(self)

# Kullanım
shapes = [Circle(10), Rectangle(5, 6)]

area_calculator = AreaCalculator()
drawing_tool = DrawingTool()

for shape in shapes:
    shape.accept(area_calculator)
    shape.accept(drawing_tool)
# Output:
# Circle area: 314.0
# Drawing a circle with radius 10
# Rectangle area: 30
# Drawing a rectangle with width 5 and height 6

print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# Visitor Arayüzü
class FileSystemVisitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass
    
    @abstractmethod
    def visit_directory(self, directory):
        pass

# Concrete Visitor Sınıfları
class SizeCalculator(FileSystemVisitor):
    def __init__(self):
        self.total_size = 0

    def visit_file(self, file):
        self.total_size += file.size
    
    def visit_directory(self, directory):
        for element in directory.elements:
            element.accept(self)
    
    def get_total_size(self):
        return self.total_size

class FileLister(FileSystemVisitor):
    def __init__(self):
        self.files = []

    def visit_file(self, file):
        self.files.append(file.name)
    
    def visit_directory(self, directory):
        for element in directory.elements:
            element.accept(self)
    
    def get_files(self):
        return self.files

# Element Arayüzü
class FileSystemElement(ABC):
    @abstractmethod
    def accept(self, visitor: FileSystemVisitor):
        pass

# Concrete Element Sınıfları
class File(FileSystemElement):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_file(self)

class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.elements = []
    
    def add_element(self, element):
        self.elements.append(element)
    
    def accept(self, visitor: FileSystemVisitor):
        visitor.visit_directory(self)

# Kullanım
root = Directory("root")
file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)
subdir = Directory("subdir")
file3 = File("file3.txt", 300)

root.add_element(file1)
root.add_element(file2)
root.add_element(subdir)
subdir.add_element(file3)

# Dosya boyutlarını hesapla
size_calculator = SizeCalculator()
root.accept(size_calculator)
print(f"Total size: {size_calculator.get_total_size()} bytes")
# Output: Total size: 600 bytes

# Dosya listesini al
file_lister = FileLister()
root.accept(file_lister)
print("Files:", file_lister.get_files())
# Output: Files: ['file1.txt', 'file2.txt', 'file3.txt']
