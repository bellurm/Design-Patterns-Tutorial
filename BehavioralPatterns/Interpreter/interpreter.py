# ÖRNEK 1
from abc import ABC, abstractmethod

# AbstractExpression (Soyut İfade)
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# TerminalExpression (Terminal İfade)
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# NonTerminalExpression (Non-Terminal İfade)
class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.variables.get(self.name, 0)  # Değişken değeri yoksa 0 olarak varsayalım

class Addition(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Context (Bağlam)
class Context:
    def __init__(self):
        self.variables = {}

# Kullanım
context = Context()
context.variables['x'] = 10
context.variables['y'] = 5

# İfadeler oluşturuluyor
expression = Addition(Variable('x'), Variable('y'))
result = expression.interpret(context)
print("Sonuç:", result)  # Çıktı: 15


print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod
import re

# AbstractExpression (Soyut İfade)
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# TerminalExpression (Terminal İfade)
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# NonTerminalExpression (Non-Terminal İfade)
class Addition(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtraction(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiplication(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Division(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

# Context (Bağlam)
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

# Kullanım
context = Context()
context.set_variable('x', 10)
context.set_variable('y', 5)

# İfade oluşturma
expression = Addition(Number(context.variables['x']), Multiplication(Number(2), Number(context.variables['y']))) # 10 + 5 * 2

# İfadeyi yorumla ve sonucu ekrana yazdır
result = expression.interpret()
print("Sonuç:", result)  # Çıktı: 20
