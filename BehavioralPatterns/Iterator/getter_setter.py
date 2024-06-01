class Person:
    def __init__(self, name, age):
        self._name = name  # Özel değişken
        self._age = age    # Özel değişken

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

# Kullanım
person = Person("John Doe", 30)
print(f"Name: {person.name}, Age: {person.age}")

person.name = "Jane Doe"  # Geçerli isim
person.age = 25           # Geçerli yaş
print(f"Updated Name: {person.name}, Updated Age: {person.age}")

try:
    person.name = 123  # Geçersiz isim, ValueError fırlatır
except ValueError as e:
    print(e)

try:
    person.age = -5  # Geçersiz yaş, ValueError fırlatır
except ValueError as e:
    print(e)
