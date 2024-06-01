# Modül ile kopyalama
import copy

# Sığ Kopyalama Örneği
original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)  # Sığ kopyalama

shallow_copy[1][0] = 'a'
print("Original List (Shallow Copy):", original_list)  # [1, ['a', 3], 4]
print("Shallow Copy:", shallow_copy)                   # [1, ['a', 3], 4]

# Derin Kopyalama Örneği
original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)  # Derin kopyalama

deep_copy[1][0] = 'a'
print("Original List (Deep Copy):", original_list)     # [1, [2, 3], 4]
print("Deep Copy:", deep_copy)                         # [1, ['a', 3], 4]

####################################################################################################
print("#"*100)
####################################################################################################

# Manuel kopyalama
class Prototype:
    def clone(self):
        # Klonlama işlemi manuel olarak gerçekleştirilir
        pass

class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return ConcretePrototype1(self.value)

    def __str__(self):
        return f"ConcretePrototype1 with value: {self.value}"

# Kullanım
prototype1 = ConcretePrototype1(10)
clone1 = prototype1.clone()
print(clone1)  # ConcretePrototype1 with value: 10

