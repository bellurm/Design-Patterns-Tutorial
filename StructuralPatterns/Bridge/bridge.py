# ÖRNEK 1
# Implementor (Gerçekleştirici) Arayüzü
from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass


# ConcreteImplementor (Somut Gerçekleştirici) Sınıfları
class RedColor(Color):
    def apply_color(self):
        return "Applying red color"

class BlueColor(Color):
    def apply_color(self):
        return "Applying blue color"


# Abstraction (Soyutlama) Sınıfı
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


# RefinedAbstraction (Gelişmiş Soyutlama) Sınıfları
class Circle(Shape):
    def draw(self):
        return f"Circle drawn. {self.color.apply_color()}"

class Square(Shape):
    def draw(self):
        return f"Square drawn. {self.color.apply_color()}"

# Kullanım
red_color = RedColor()
blue_color = BlueColor()

circle = Circle(red_color)
square = Square(blue_color)

print(circle.draw())  # Output: Circle drawn. Applying red color
print(square.draw())  # Output: Square drawn. Applying blue color

print("#" * 60)

# ÖRNEK 2
from abc import ABC, abstractmethod

class PrinterImplementor(ABC):
    @abstractmethod
    def print_document(self, document: str) -> str:
        pass


class PlainTextPrinter(PrinterImplementor):
    def print_document(self, document: str) -> str:
        return f"Printing plain text: {document}"

class HtmlPrinter(PrinterImplementor):
    def print_document(self, document: str) -> str:
        return f"Printing HTML: {document}"


class Printer:
    def __init__(self, printer_impl: PrinterImplementor):
        self.printer_impl = printer_impl

    def print(self, document: str) -> str:
        return self.printer_impl.print_document(document)


class Document:
    def __init__(self, content: str):
        self.content = content

class PlainTextDocument(Document):
    pass

class HtmlDocument(Document):
    pass


# Kullanım
plain_text_printer = PlainTextPrinter()
html_printer = HtmlPrinter()

plain_text_document = PlainTextDocument("This is a plain text document.")
html_document = HtmlDocument("<h1>This is an HTML document.</h1>")

print(plain_text_printer.print_document(plain_text_document.content))
print(html_printer.print_document(html_document.content))
