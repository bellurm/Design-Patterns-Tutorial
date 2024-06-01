from abc import ABC, abstractmethod

# Visitor Arayüzü
class Visitor(ABC):
    def visit(self, element):
        method_name = f'visit_{element.__class__.__name__.lower()}'
        method = getattr(self, method_name, self.generic_visit)
        method(element)

    def generic_visit(self, element):
        print(f'No visit_{element.__class__.__name__.lower()} method')

# Element Arayüzü
class Element(ABC):
    def accept(self, visitor: Visitor):
        visitor.visit(self)

# Concrete Elements
class ElementA(Element):
    pass

class ElementB(Element):
    pass

# Concrete Visitor
class ConcreteVisitor(Visitor):
    def visit_elementa(self, element):
        print("Visited ElementA")

    def visit_elementb(self, element):
        print("Visited ElementB")

# Kullanım
elements = [ElementA(), ElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)
# Output:
# Visited ElementA
# Visited ElementB
