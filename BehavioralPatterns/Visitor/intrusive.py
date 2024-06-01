from abc import ABC, abstractmethod

# Visitor Arayüzü
class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass

# Element Arayüzü
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# Concrete Elements
class ElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_element_b(self)

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Visited ElementA")

    def visit_element_b(self, element):
        print("Visited ElementB")

# Kullanım
elements = [ElementA(), ElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)
# Output:
# Visited ElementA
# Visited ElementB
