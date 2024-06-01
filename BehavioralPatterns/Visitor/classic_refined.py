from abc import ABC, abstractmethod

# Visitor Arayüzü
class Visitor(ABC):
    @abstractmethod
    def visit(self, element):
        pass

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit(self, element):
        element.accept_visitor(self)

    def visit_element_a(self, element):
        print("Visited ElementA")

    def visit_element_b(self, element):
        print("Visited ElementB")

# Element Arayüzü
class Element(ABC):
    @abstractmethod
    def accept_visitor(self, visitor: Visitor):
        pass

# Concrete Elements
class ElementA(Element):
    def accept_visitor(self, visitor: Visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept_visitor(self, visitor: Visitor):
        visitor.visit_element_b(self)

# Kullanım
elements = [ElementA(), ElementB()]
visitor = ConcreteVisitor()

for element in elements:
    visitor.visit(element)
# Output:
# Visited ElementA
# Visited ElementB
